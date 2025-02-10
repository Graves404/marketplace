import json

import aio_pika
from aio_pika import connect_robust

RABBITMQ_URL = "amqp://guest:guest@localhost/"

async def send_to_queue(message: dict):
    connection = await connect_robust(RABBITMQ_URL)
    async with connection as conn:
        ch = await conn.channel()
        queue = await ch.declare_queue("email_queue", durable=True)

        await ch.default_exchange.publish(
            aio_pika.Message(body=json.dumps(message).encode()),
            routing_key=queue.name
        )
