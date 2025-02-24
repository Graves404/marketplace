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
        user = User(**data)
        session.add(user)
        await session.commit()
        return {"msg": "User added"}

    @classmethod
    async def get_id_current_user(cls, email_: str, session: AsyncSession):
        query = (select(User.id).filter(User.email == email_))
        result_query = await session.execute(query)
        return result_query.scalar_one()

    @deprecated('Now we dont know which one data will be on frontend. Next time this method will be update', category=None)
    @classmethod
    async def refresh_data_user(cls, id_user_: int, user_update_data: UserUpdatePostDTO, session: AsyncSession):
        query = (select(User).filter(User.id == id_user_))
        result_query = await session.execute(query)
        user = result_query.scalars().first()
        if not user:
            return {"msg": "user not found"}
        val_user = Validation.validation_data(user, user_update_data)
        await session.commit()
        await session.refresh(val_user)
        return {"msg": "Done"}

    @classmethod
    async def reset_password_repository(cls, session: AsyncSession):
        try:
            await session.commit()
            return {"msg": "Password updated"}
        except:
            return {"msg": "Error, please call to support"}

    @classmethod
    async def update_password(cls, id_: int, new_password: str, session: AsyncSession):
        query = (select(User).filter(User.id == id_))
        result_query = await session.execute(query)
        user = result_query.scalars().first()
        if not user:
            return {"msg": "User not found"}
        user.hash_pass = new_password
        await session.commit()
        await session.refresh(user)
        return {"msg": "Password was updated"}


    @classmethod
    async def delete_user(cls, id_user: int, session: AsyncSession):
        if id_user is not None:
            query = (delete(User).filter(User.id == id_user))
            await session.execute(query)
            await session.commit()
        return {"msg": f"User {id_user} deleted"}

    @classmethod
    async def activate_user(cls, user: User, session: AsyncSession):
        try:
            await session.flush()
            await session.commit()
            await session.refresh(user)
            return "Account activated"
        except:
            return "Account not activated"
