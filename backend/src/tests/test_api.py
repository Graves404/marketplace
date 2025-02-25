import pytest
import pytest_asyncio
from httpx import AsyncClient, ASGITransport

from ..main import app

@pytest.fixture
async def async_client():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        yield ac

@pytest.mark.asyncio
async def test_get_all_users(async_client: AsyncClient):
    response = await async_client.get("/user/all")
    assert response.status_code == 200

@pytest.mark.asyncio
async def test_registration_user(async_client: AsyncClient):
    response = await async_client.post("/user/registration_service", json=get_payload())
    assert response.status_code == 200

@pytest.mark.asyncio
async def test_update_data_of_user(async_client: AsyncClient):
    auth_payload = {
        "email": "john.doe@test.com",
        "hash_pass": "string"
    }
    auth_response = await async_client.post("/authentication/check_user", json=auth_payload)
    print(auth_response.json())
    assert auth_response.status_code == 200

def get_payload():
    return {
        "name": "John",
        "surname": "Doe",
        "email": "john.doe@test.com",
        "city": "New York",
        "phone": "+1 202-965-1420",
        "username": "JohnDoe",
        "is_active": False,
        "hash_pass": "string"
    }

def get_payload_update():
    return {
        "name": "John",
        "surname": "Doe",
        "email": "john.doe@test.com",
        "city": "Washington D.C.",
        "phone": "+1 202-965-1420",
        "username": "JohnCooler",
        "is_active": True
    }
