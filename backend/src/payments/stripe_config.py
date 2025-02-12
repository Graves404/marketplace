from ..settings.config import settings
import stripe

class StripeConfig:

    SECRET_KEY_STRIPE = settings.SECRET_KEY_STRIPE

    MARKET_DOMAIN = 'http://localhost:3000'

    stripe.api_key = SECRET_KEY_STRIPE
    @classmethod
    async def payment(cls):
        payment = stripe.PaymentIntent.create(
            amount=amount_*100,
            currency="eur",
            payment_method_types=["card"],
        )

        return payment.client_secret

    @classmethod
    async def create_payment_session(cls, title: str, price: int):
        try:
            checkout_session = stripe.checkout.Session.create(
                line_items=[
                    {
                        "price_data": {
                            "currency": "eur",
                            "product_data": {
                                "name": f"{title}"
                            },
                            "unit_amount": price * 100
                        },
                        "quantity": 1,
                    }
                ],
                mode="payment",
                success_url=YOUR_DOMAIN + "/return?session_id={CHECKOUT_SESSION_ID}",
                cancel_url=YOUR_DOMAIN + "/checkout",
            )
        except Exception as e:
            return str(e)

        return await jsonify(sessionId=checkout_session.id)
