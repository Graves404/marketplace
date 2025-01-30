from ..queries.user_repository import UserRepository
from ..queries.auth_repository import AuthRepository
from .jwt_service import JwtService
from ..pydantic_schemas.schemas import UserRelDTO, UserDTO, UserRegistrationDTO
from ..security.hash_pass import hash_password
from ..pydantic_schemas.schemas import UserUpdatePostDTO, UserUpdatePasswordDTO
from fastapi import Request, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

class User:
    @classmethod
    async def get_list_users(cls, session: AsyncSession) -> list[UserDTO]:
        result_orm = await UserRepository.get_users_list(session)
        result_dto = [UserDTO.model_validate(row, from_attributes=True) for row in result_orm]
        return result_dto


    @classmethod
    async def registration(cls, user: UserRegistrationDTO, session: AsyncSession):
        user.hash_pass = hash_password(user.hash_pass)
        data = user.model_dump()
        return await UserRepository.registration_user(data, session)

    @classmethod
    async def get_id_current_user(cls, email_: str, session: AsyncSession):
        return await UserRepository.get_id_current_user(email_, session)

    @classmethod
    async def update_data_user(cls, req: Request, update_user: UserUpdatePostDTO, session: AsyncSession):
        token = req.headers.get("Authorization")
        user_id = JwtService.get_id_user_token(token)
        res = await UserRepository.refresh_data_user(user_id, update_user, session)
        return {f"{user_id}": res}


    @classmethod
    async def update_password(cls, req: Request, user: UserUpdatePasswordDTO, session: AsyncSession):
        data = user.model_dump()
        if AuthRepository.authentication(data, session):
            token = req.headers.get("Authorization")
            user_id = JwtService.get_id_user_token(token)
            return await UserRepository.update_password(user_id, hash_password(user.new_pass), session)
        raise HTTPException(status_code=403, detail="Incorrect password or email")

    @classmethod
    async def delete_user(cls, req: Request, session: AsyncSession):
        token = req.headers.get("Authorization")
        user_id = JwtService.get_id_user_token(token)
        #TODO: DELETE IMAGES FROM A CLOUD STORAGE
        return await UserRepository.delete_user(user_id, session)

    @classmethod
    async def get_user_info(cls, req: Request, session: AsyncSession):
        token = req.headers.get("Authorization")
        user_id = JwtService.get_id_user_token(token)
        user = await UserRepository.get_user_by_id(user_id, session)
        return UserRelDTO.model_validate(user, from_attributes=True)