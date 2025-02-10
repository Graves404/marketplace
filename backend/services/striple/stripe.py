import os
from dotenv import load_dotenv

import stripe
import json


load_dotenv()

STRIPE_API_KEY = os.getenv("PUBLISH_KEY_STRIPE")
STRIPE_DOMAIN = os.getenv("SECRET_KEY_STRIPE")

stripe.api_key = STRIPE_API_KEY

async def create_payment(amount: int, currency: str, token: str):
    try:
      charge = stripe.Charge.create(
          amount=amount,
          currency=currency,
          source=token,
          description="Payment for FastAPI Store")
      return {"status": "success", "charger_id": charge.id}
    except stripe.error.CardError as e:
        return {"status": "error", "message": str(e)}
    except stripe.error.StripeError as e:
        return {"status": "error", "message": str(e)}
