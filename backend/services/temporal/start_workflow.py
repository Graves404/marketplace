from temporalio.client import Client
import asyncio

async def start_workflow(email: str):

    client = await Client.connect("localhost:7233", namespace="default")

    await client.start_workflow(
        "UserRegistrationWorkflow",
        email,
        id="user-registration-workflow-id",
        task_queue="email-task-queue"
    )

    print("✅ Workflow start!")

if __name__ == "__main__":
    asyncio.run(start_workflow("m.derkaqw@gmail.com"))