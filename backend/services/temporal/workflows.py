import datetime

from temporalio import workflow
from activities import send_verification_email

@workflow.defn
class UserRegistrationWorkflow:
    @workflow.run
    async def verifi_email(self, email: str):
        await workflow.execute_activity(
            send_verification_email,
            email,
            schedule_to_close_timeout=datetime.timedelta(seconds=30)
        )
        print(f"📩 Waiting confirm email {email}")