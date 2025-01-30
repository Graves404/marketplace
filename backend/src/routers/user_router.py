from typing import Annotated

from fastapi import APIRouter, Depends, Request
from fastapi.security import OAuth2PasswordBearer
from ..security.security_config import security
from ..pydantic_schemas.schemas import UserDTO, UserRegistrationDTO, UserUpdatePasswordDTO
from ..service.user_service import User
from ..pydantic_schemas.schemas import UserUpdatePostDTO
from sqlalchemy.ext.asyncio import AsyncSession
from ..engine_database.database import get_async_session_factory

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

user_router = APIRouter(
    prefix="/user"
)

@user_router.get("/all")
async def get_all_users(session: AsyncSession = Depends(get_async_session_factory)) -> list[UserDTO]:
    return await User.get_list_users(session)

@user_router.post("/registration_service")
async def registration(user: UserRegistrationDTO, session: AsyncSession = Depends(get_async_session_factory)):
    return await User.registration(user, session)


@user_router.put("/update_data", dependencies=[Depends(security.access_token_required)])
async def update_data_of_user(req: Request, update_user: UserUpdatePostDTO, session: AsyncSession = Depends(get_async_session_factory)):
    return await User.update_data_user(req, update_user, session)

@user_router.post("/update_password", dependencies=[Depends(security.access_token_required)])
async def update_password_user(req: Request, user: UserUpdatePasswordDTO, session: AsyncSession = Depends(get_async_session_factory)):
    return await User.update_password(req=req, user=user, session=session)

@user_router.post("/delete_user", dependencies=[Depends(security.access_token_required)])
async def delete_current_user(req: Request, session: AsyncSession = Depends(get_async_session_factory)):
    return await User.delete_user(req, session)

@user_router.get("/my_profile", dependencies=[Depends(security.access_token_required)])
async def my_profile(req: Request, session: AsyncSession = Depends(get_async_session_factory)):
    return await User.get_user_info(req, session)

