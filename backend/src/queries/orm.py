from ..data_models.models import User, Items, Images
from sqlalchemy import select
from ..database import session_factory, async_session_factory
from ..pydantic_schemas.schemas import UserDTO, UserRelDTO, PasswordDTO
from sqlalchemy.orm import selectinload
from ..security.hash_pass import hash_password, verify_hash_pass

@staticmethod
async def async_select_user():
   async with async_session_factory() as session:
        query = (select(User).limit(10))
        res = await session.execute(query)
        result_orm = res.scalars().all()
        result_dto = [UserDTO.model_validate(row, from_attributes=True) for row in result_orm]
        return result_dto

@staticmethod
async def async_select_current_user(id_: int):
    async with async_session_factory() as session:
        query = (select(User).filter(User.id == id_).options(selectinload(User.items)))
        res = await session.execute(query)
        user_orm = res.scalars().all()
        return [UserRelDTO.model_validate(row, from_attributes=True) for row in user_orm]


@staticmethod
async def get_user_id(email_: str):
    async with async_session_factory() as session:
        query = (
            select(User.id).filter(User.email == email_)
        )
        res = await session.execute(query)
        return res.scalar_one()

@staticmethod
async def insert_item(title_: str, description_: str, price_: int, city_: str, user_id_: int, url_files_: list[str]):
    item = Items(title=title_, description=description_, price=price_, city=city_, user_id=user_id_)
    async with async_session_factory() as session:
        try:
            session.add(item)
            await session.flush()
            images = [
                Images(url_photo=url, items_id=item.id)
                for url in url_files_
            ]
            session.add_all(images)
            await session.commit()
            return {"msg", f"item {title_} added and photo {len(url_files_)}"}
        except Exception as e:
            await session.rollback()
            raise e

@staticmethod
async def async_insert_user(_username: str, _password: str, _name: str, _surname: str, _email: str, _city: str,_phone: str):
    _hash_pass = hash_password(_password)
    new_user = User(name=_name, surname=_surname, email=_email, city=_city, phone=_phone, username=_username, hash_pass=_hash_pass)

    async with async_session_factory() as session:
        session.add(new_user)
        await session.commit()
    return {"msg": f"User {_username} added"}




@staticmethod
def get_user_items():
    with session_factory() as session:
        query = (
            select(User).options(selectinload(User.items))
            .limit(10)
        )
        res = session.execute(query)
        result_orm = res.scalars().all()

        result_dto = [UserDTO.model_validate(row, from_attributes=True) for row in result_orm]
        return result_dto


@staticmethod
def get_hash_password(username_: str):
    with session_factory() as session:
        query = (
            select(User).filter(User.username == username_)
        )

        res = session.execute(query)
        result_orm = res.scalars().all()
        return [PasswordDTO.model_validate(row, from_attributes=True) for row in result_orm]


@staticmethod
def get_user_by_username(username_: str):
    with session_factory() as session:
        query = (
            select(User).filter(User.username == username_)
        )

        res = session.execute(query)
        result_orm = res.scalars().all()
        return [UserRelDTO.model_validate(row, from_attributes=True) for row in result_orm]

@staticmethod
async def check_hash(email_: str, password_: str):
    async with async_session_factory() as session:
        query = (
            select(User.hash_pass).filter(User.email == email_)
        )
        hash_storage = session.execute(query).scalar_one()
        return await verify_hash_pass(password_, hash_storage)

