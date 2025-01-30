import os
from dotenv import load_dotenv
from temporalio import activity
import aiohttp

load_dotenv()

MAILGUN_API_KEY = os.getenv("MAILGUN_API_KEY")
MAILGUN_DOMAIN = os.getenv("MAILGUN_DOMAIN")

@activity.defn
async def send_verification_email(email: str):
    url = f"https://api.mailgun.net/v3/{MAILGUN_DOMAIN}/messages"
    auth = aiohttp.BasicAuth("api", MAILGUN_API_KEY)
    data = {
            "from": "Excited User <mailgun@sandbox040a4dd43920480eab793830cec6072b.mailgun.org>",
            "to": [email, f"{email}@sandbox040a4dd43920480eab793830cec6072b.mailgun.org"],
            "subject": "Hello from Temporal",
            "text": "Use the temporal and mailgun - awesome"
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(url, auth=auth, data=data) as response:
            if response.status == 200:
                print("The message send")
            else:
                print(f"Error {response.status}")
