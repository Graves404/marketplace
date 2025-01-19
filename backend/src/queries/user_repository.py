from ..data_models.models import User
from sqlalchemy import select
from ..database import async_session_factory
from sqlalchemy.orm import selectinload
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
