from ..queries.user_repository import UserRepository
from ..queries.auth_repository import AuthRepository
from .jwt_service import JwtService
from ..pydantic_schemas.schemas import UserRelDTO, UserDTO, UserRegistrationDTO
from ..security.hash_pass import hash_password
from ..pydantic_schemas.schemas import UserUpdatePostDTO, UserUpdatePasswordDTO
from fastapi import Request, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from ..rabbit_mq.producer import send_to_queue_email, send_to_queue_reset_password
from pydantic import EmailStr

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
        new_user = await UserRepository.registration_user(data, session)
        email_task = {"email": user.email, "subject": "Welcome!", "message": "Thanks for registered"}
        await send_to_queue_email(email_task)
        return new_user

    @classmethod
    async def get_id_current_user(cls, email_: str, session: AsyncSession):
        return await UserRepository.get_id_current_user(email_, session)

    @classmethod
    async def forget_password_service(cls, email: str, session: AsyncSession):
        try:
            user = await UserRepository.get_current_user(email, session)
            if user is not None:
                email_task = {"email": user.email, "subject": "Reset Password", "message": "Please don't show nobody a new pass"}
                await send_to_queue_reset_password(email_task)
            else:
                return {"msg": "User is not found"}
        except:
            return {"msg": "User is not found"}
        return {"msg": "Created a new password"}

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

    @classmethod
    async def activate_service(cls, email: EmailStr, session: AsyncSession):
        user = await UserRepository.get_current_user(email_=email, session=session)
        user.is_active = True
        return await UserRepository.activate_user(user=user, session=session)