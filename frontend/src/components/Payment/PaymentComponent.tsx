import React, { useState } from "react";
import PaymentData from "../../models/PaymentData";
import { Button } from "antd";
import { loadStripe } from "@stripe/stripe-js";

const stripePromise = loadStripe("pk_test_51QoiqPENMJnJWjcUqP6VLLozyGCThWqsx1lDZLSLww6YT0WcSYfwOPrC0CFAHvZxixcUUDyMvgUTFanR9TAZWLuC00tcTzxVkB");

const PaymentComponent: React.FC<PaymentData> = ({ title, price }) => {
  
  const [ loading, setLoading ] = useState<boolean>(false);

  const handleCheckout = async () => {
    setLoading(true);

    try {
      const response = await fetch("http://localhost:8000/items/payment_item_session", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({title, price}),
        });

        const data = await response.json();

        if(!data.sessionId) {
          throw new Error("Session ID not received");
        }

        const stripe = await stripePromise;

        if(!stripe) {
          throw new Error("Stripe failed to initialize");
        }

        const { error } = await stripe.redirectToCheckout({
          sessionId: data.sessionId,
        });

        if (error) {
          console.error("Stripe Checkout error:", error);
        }

    } catch (error) {
      console.error(error);
    } finally {
      setLoading(false);
    }
  }
  
  return(
    <div className="flex justify-center">
      <Button onClick={handleCheckout} color="blue" variant="solid" size="large">
        <p className="text-2xl">{loading ? "Loading..." : `Pay`}</p>
      </Button>
    </div>
  )
}

export default PaymentComponent;