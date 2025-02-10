from temporalio.worker import Worker
from temporalio.client import Client
from activities import send_verification_email
from workflows import UserRegistrationWorkflow
import asyncio

async def main():

    client = await Client.connect("localhost:7233", namespace="default")

    worker: Worker = Worker(
        client,
        task_queue="email-task-queue",
        workflows=[UserRegistrationWorkflow],
        activities=[send_verification_email]

    )
    await worker.run()

if __name__ == "__main__":
    asyncio.run(main())
