import os
from dotenv import load_dotenv
from temporalio import activity
import aiohttp

load_dotenv()

MAILGUN_API_KEY = os.getenv("MAILGUN_API_KEY")
MAILGUN_DOMAIN = os.getenv("MAILGUN_DOMAIN")

@activity.defn(name="verification_email")
async def send_verification_email(email: str):
    url = f"https://api.mailgun.net/v3/{MAILGUN_DOMAIN}/messages"
    auth = aiohttp.BasicAuth("api", MAILGUN_API_KEY)
    data = {
            "from": "Menu 7/52 Test <mailgun@sandbox040a4dd43920480eab793830cec6072b.mailgun.org>",
            "to": [email, f"{email}@sandbox040a4dd43920480eab793830cec6072b.mailgun.org"],
            "subject": "Registration",
            "template": "test_action",
            "h:X-Mailgun-Variables": '{"test": "test"}'
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(url, auth=auth, data=data) as response:
            if response.status == 200:
                print("The message send")
            else:
                print(f"Error {response.status}")
