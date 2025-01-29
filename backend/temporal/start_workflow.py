from temporalio.client import Client
import asyncio

async def start_workflow():
    client = await Client.connect("localhost:7233")

    await client.start_workflow(
        "UserRegistrationWorkflow",
        "m.derkaqw@gmail.com",
        id="user-registration-workflow-id",
        task_queue="email-task-queue"
    )

    print("✅ Workflow start!")

if __name__ == "__main__":
    asyncio.run(start_workflow())