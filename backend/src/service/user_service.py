from ..queries.user_repository import UserRepository
from .jwt_service import JwtService
from ..pydantic_schemas.schemas import UserRelDTO, UserDTO
from ..security.hash_pass import hash_password
from ..data_models.update_data_validation import Validation
from fastapi import Request


class User:
    @classmethod
    async def get_current_user_by_email(cls, email_: str):
        result_orm = await UserRepository.get_current_user(email_)
        result_dto = [UserRelDTO.model_validate(row, from_attributes=True) for row in result_orm]
        return result_dto

    @classmethod
    async def get_list_users(cls) -> list[UserDTO]:
        result_orm = await UserRepository.get_users_list()
        result_dto = [UserDTO.model_validate(row, from_attributes=True) for row in result_orm]
        return result_dto

    @classmethod
    async def registration(cls, _username: str, _password: str, _name: str, _surname: str, _email: str, _city: str, _phone: str):
        _hash = hash_password(_password)
        return await UserRepository.registration_user(_username, _hash, _name, _surname, _email, _city, _phone)

    @classmethod
    async def get_id_current_user(cls, email_: str):
        return await UserRepository.get_id_current_user(email_)

    @classmethod
    async def update_data_user(cls,  _username: str, _name: str, _surname: str, _email: str, _city: str, _phone: str):
        # logic of validation
        validation_user = Validation.validation_data(_username, _name, _surname, _email, _city, _phone)
        print(validation_user.email)
        return {"data": validation_user}

    @classmethod
    async def update_password(cls, old_password: str, new_password: str):
        new_hash = hash_password(new_password)
        return await ...

    @classmethod
    async def delete_user(cls, req: Request):
        token = req.cookies.get("mne_market_accesses_token")
        user_id = JwtService.get_id_user_token(token)
        return await UserRepository.delete_user(user_id)

# TODO: add more function:
#  1. "refresh" Update information about user (User can to change information self) - because this method has check of validation
#  2. "Change Password" user should have function of change password