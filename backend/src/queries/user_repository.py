from ..data_models.models import User
from sqlalchemy import select, delete
from ..engine_database.database import async_session_factory
from sqlalchemy.orm import selectinload
from ..pydantic_schemas.schemas import UserUpdatePostDTO
from ..data_models.update_data_validation import Validation
from typing_extensions import deprecated
class UserRepository:
    @classmethod
    async def get_users_list(cls):
        async with async_session_factory() as session:
            query = (select(User))
            start_query = await session.execute(query)
            result = start_query.scalars().all()
            return result

    @classmethod
    async def get_current_user(cls, email_: str):
        async with async_session_factory() as session:
            query = (select(User).filter(User.email == email_).options(selectinload(User.items)))
            start_query = await session.execute(query)
            result = start_query.scalars().all()
            return result

    @classmethod
    async def registration_user(cls, _username: str, _password: str, _name: str, _surname: str, _email: str,
                                _city: str, _phone: str):

            new_user = User(name=_name, surname=_surname, email=_email, city=_city, phone=_phone, username=_username,
                            hash_pass=_password)

            async with async_session_factory() as session:
                session.add(new_user)
                await session.commit()
            return {"msg": f"User {_username} added"}

    @classmethod
    async def get_id_current_user(cls, email_: str):
        async with async_session_factory() as session:
            query = (select(User.id).filter(User.email == email_))
            res = await session.execute(query)
            return res.scalar_one()

    @deprecated('Now we dont know which one data will be on frontend. Next time this method will be update', category=None)
    @classmethod
    async def refresh_data_user(cls, id_user_: int, user_update_data: UserUpdatePostDTO):
        async with async_session_factory() as session:
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
    async def update_password(cls, id_: int, new_password: str):
        async with async_session_factory() as session:
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
    async def delete_user(cls, id_user: int):
        async with async_session_factory() as session:
            if id_user is not None:
                query = (delete(User).filter(User.id == id_user))
                await session.execute(query)
                await session.commit()
            return {"msg": f"User {id_user} deleted"}
