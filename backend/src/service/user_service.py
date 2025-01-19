from ..queries.user_repository import UserRepository
from ..pydantic_schemas.schemas import UserRelDTO, UserDTO
from ..security.hash_pass import hash_password


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
