import json
import sys
import os
import asyncio

import aiohttp
import httpx
import aio_pika
from pydantic import ValidationError
from dotenv import load_dotenv

sys.path.append("..")
from pydantic_schemas.schemas import EmailRabbitSchemas

load_dotenv()

RABBITMQ_URL = "amqp://guest:guest@localhost/"
MAILGUN_API_KEY = os.getenv("MAILGUN_API_KEY")
MAILGUN_DOMAIN = os.getenv("MAILGUN_DOMAIN")
MAILGUN_URL = f"https://api.mailgun.net/v3/{MAILGUN_DOMAIN}/messages"


async def send_registration_email(email, subject, message):
    auth = aiohttp.BasicAuth("api", MAILGUN_API_KEY)
    data = {"from": "Kupi.mne <postmaster@sandbox040a4dd43920480eab793830cec6072b.mailgun.org>",
            "to": f"Dmitrii <{email}>",
            "subject": subject,
            "template": "verification_email",
            "h:X-Mailgun-Variables": json.dumps({
                "confirm_url": f"http://127.0.0.1:8000/user/verification_address/{email}"
            })
            }

    async with httpx.AsyncClient() as client:
        response = await client.post(url=MAILGUN_URL, auth=auth, data=data)

        return response.status_code

async def send_recovery_email(email, subject, message):
    auth = aiohttp.BasicAuth("api", MAILGUN_API_KEY)
    data = {"from": "Kupi.mne <postmaster@sandbox040a4dd43920480eab793830cec6072b.mailgun.org>",
            "to": f"Dmitrii <{email}>",
            "subject": subject,
            "template": "forget password",
            "h:X-Mailgun-Variables": json.dumps({
                "reset_url": f"http://localhost:5173/reset_password/{email}"
            })
            }

    async with httpx.AsyncClient() as client:
        response = await client.post(url=MAILGUN_URL, auth=auth, data=data)

        return response.status_code

async def process_registration(message: aio_pika.IncomingMessage):
    async with message.process() as msg:
        try:
            data = json.loads(msg.body.decode('utf-8'))
            email_schemas = EmailRabbitSchemas(**data)
            await send_registration_email(email=email_schemas.email, subject=email_schemas.subject, message=email_schemas.message)
        except ValidationError as e:
            print(f"Error {e}")

async def process_reset_password(message: aio_pika.IncomingMessage):
    async with message.process() as msg:
        try:
            data = json.loads(msg.body.decode('utf-8'))
            email_schemas = EmailRabbitSchemas(**data)
            await send_recovery_email(email=email_schemas.email, subject=email_schemas.subject, message=email_schemas.message)
        except ValidationError as e:
            print(f"Error {e}")


async def main():
    connection = await aio_pika.connect_robust(RABBITMQ_URL)
    async with connection as conn:
        async with conn.channel() as ch:
            registration_queue = await ch.declare_queue(name="email_registration_queue", durable=True)
            await registration_queue.consume(process_registration)
            reset_password_queue = await ch.declare_queue(name="reset_password_queue", durable=True)
            await reset_password_queue.consume(process_reset_password)
            await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
