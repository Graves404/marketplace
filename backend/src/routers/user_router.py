from fastapi import APIRouter

from ..queries.orm import async_select_user, async_select_current_user, async_insert_user
from ..pydantic_schemas.schemas import UserDTO


user_router = APIRouter(
    prefix="/user"
)

@user_router.get("/all")
async def get_all_users() -> list[UserDTO]:
    return await async_select_user()

@user_router.get("/get_current_user/{id}")
async def get_current_user(id_: int):
    return await async_select_current_user(id_)

@user_router.post("/registration")
async def registration(username_: str, password_: str, name_: str, surname_: str, email_: str, city_: str, phone_: str):
    return await async_insert_user(username_, password_, name_, surname_, email_, city_, phone_)
