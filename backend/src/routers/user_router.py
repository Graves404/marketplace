from fastapi import APIRouter, Depends, Request
from ..security.security_config import security
from ..pydantic_schemas.schemas import UserDTO
from ..service.user_service import User
from ..pydantic_schemas.schemas import UserUpdatePostDTO


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

@user_router.put("/update_data", dependencies=[Depends(security.access_token_required)])
async def update_data_of_user(req: Request, update_user: UserUpdatePostDTO):
    return await User.update_data_user(req, update_user)

@user_router.post("/update_password", dependencies=[Depends(security.access_token_required)])
async def update_password_user(req: Request, email: str, old_password_: str, new_password_: str):
    return await User.update_password(req=req, email=email, old_password=old_password_, new_password=new_password_)

@user_router.post("/delete_user", dependencies=[Depends(security.access_token_required)])
async def delete_current_user(req: Request):
    return await User.delete_user(req)
