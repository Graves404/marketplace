from fastapi import APIRouter

from ..pydantic_schemas.schemas import UserDTO
from ..service.user_service import User


user_router = APIRouter(
    prefix="/user"
)

@user_router.get("/all")
async def get_all_users() -> list[UserDTO]:
    return await User.get_list_users()

@user_router.get("/get_current_user/{email}")
async def get_current_user(email: str):
    return await User.get_current_user_by_email(email)

@user_router.post("/registration_service")
async def registration(username_: str, password_: str, name_: str, surname_: str, email_: str, city_: str, phone_: str):
    return await User.registration(username_, password_, name_, surname_, email_, city_, phone_)
