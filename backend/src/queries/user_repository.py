from ..data_models.models import User, Items, Images
from sqlalchemy import select, delete
from sqlalchemy.orm import selectinload
from ..pydantic_schemas.schemas import UserUpdatePostDTO
from ..data_models.update_data_validation import Validation
from typing_extensions import deprecated
from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import EmailStr
class UserRepository:
    @classmethod
    async def get_users_list(cls, session: AsyncSession):
        query = (select(User))
        result_query = await session.execute(query)
        return result_query.scalars().all()

    @classmethod
    async def get_current_user(cls, email_: str, session: AsyncSession):
        query = (select(User).filter(User.email == email_).options(selectinload(User.items)))
        result_query = await session.execute(query)
        return result_query.scalars().first()

    @classmethod
    async def get_user_by_id(cls, id_: int, session: AsyncSession):
        query = (select(User).filter(User.id == id_).options(selectinload(User.items)))
        result_query = await session.execute(query)
        return result_query.scalars().first()

    @classmethod
    async def registration_user(cls, data: dict, session: AsyncSession):
        try:
            user = User(**data)
            session.add(user)
            await session.commit()
            return {"code": 201, "msg": "The user added"}
        except Exception as e:
            return {"code": 500, "msg": f"Problem with server {e}"}

    @classmethod
    async def get_id_current_user(cls, email_: str, session: AsyncSession):
        query = (select(User.id).filter(User.email == email_))
        result_query = await session.execute(query)
        return result_query.scalar_one()

    @classmethod
    async def refresh_data_user(cls, user_update_data: UserUpdatePostDTO, session: AsyncSession):
        await session.commit()
        await session.refresh(user_update_data)
        return {"code": 200, "msg": "Completed"}

    @classmethod
    async def reset_password_repository(cls, session: AsyncSession):
        try:
            await session.commit()
            return {"code": 200, "msg": "The password was reseted"}
        except:
            return {"code": 500, "msg": "Error, please call to support"}

    @classmethod
    async def update_password(cls, id_: int, new_password: str, session: AsyncSession):
        query = (select(User).filter(User.id == id_))
        result_query = await session.execute(query)
        user = result_query.scalars().first()
        if not user:
            return {"code": 404, "msg": "User not found"}
        user.hash_pass = new_password
        await session.commit()
        await session.refresh(user)
        return {"code": 200, "msg": "Password was updated"}


    @classmethod
    async def delete_user(cls, id_user: int, session: AsyncSession):
        if id_user is not None:
            query = (delete(User).filter(User.id == id_user))
            await session.execute(query)
            await session.commit()
        return {"code": 200, "msg": f"The user {id_user} was deleted"}

    @classmethod
    async def activate_user(cls, user: User, session: AsyncSession):
        try:
            await session.flush()
            await session.commit()
            await session.refresh(user)
            return {"code": 200, "msg": "The account was activated"}
        except:
            return {"code": 500, "msg": "The account was not activated"}
