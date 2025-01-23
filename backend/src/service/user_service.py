from ..queries.user_repository import UserRepository
from ..queries.auth_repository import AuthRepository
from .jwt_service import JwtService
from ..pydantic_schemas.schemas import UserRelDTO, UserDTO
from ..security.hash_pass import hash_password
from ..pydantic_schemas.schemas import UserUpdatePostDTO
from fastapi import Request, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

class User:
    @classmethod
    async def get_current_user_by_email(cls, email_: str, session: AsyncSession):
        result_orm = await UserRepository.get_current_user(email_, session)
        result_dto = [UserRelDTO.model_validate(row, from_attributes=True) for row in result_orm]
        return result_dto

    @classmethod
    async def get_list_users(cls, session: AsyncSession) -> list[UserDTO]:
        result_orm = await UserRepository.get_users_list(session)
        result_dto = [UserDTO.model_validate(row, from_attributes=True) for row in result_orm]
        return result_dto

    @classmethod
    async def registration(cls, _username: str, _password: str, _name: str, _surname: str, _email: str, _city: str, _phone: str, session: AsyncSession):
        _hash = hash_password(_password)
        return await UserRepository.registration_user(_username, _hash, _name, _surname, _email, _city, _phone, session)

    @classmethod
    async def get_id_current_user(cls, email_: str, session: AsyncSession):
        return await UserRepository.get_id_current_user(email_, session)

    @classmethod
    async def update_data_user(cls, req: Request, update_user: UserUpdatePostDTO, session: AsyncSession):
        token = req.cookies.get("mne_market_accesses_token")
        user_id = JwtService.get_id_user_token(token)
        res = await UserRepository.refresh_data_user(user_id, update_user, session)
        return {f"{user_id}": res}


    @classmethod
    async def update_password(cls, req: Request, email: str, old_password: str, new_password: str, session: AsyncSession):
        if AuthRepository.authentication(email, old_password, session):
            token = req.cookies.get("mne_market_accesses_token")
            user_id = JwtService.get_id_user_token(token)
            return await UserRepository.update_password(user_id, hash_password(new_password), session)
        raise HTTPException(status_code=403, detail="Incorrect password or email")

    @classmethod
    async def delete_user(cls, req: Request, session: AsyncSession):
        token = req.cookies.get("mne_market_accesses_token")
        user_id = JwtService.get_id_user_token(token)
        #TODO: DELETE IMAGES FROM A CLOUD STORAGE
        return await UserRepository.delete_user(user_id, session)
