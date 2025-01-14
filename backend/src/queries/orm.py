from models import User, Items, Password
from sqlalchemy import select
from database import engine, session_factory
from schemas import UserDTO, UserRelDTO, PasswordDTO, UserPassDTO
from sqlalchemy.orm import relationship, selectinload
from hash_pass import hash_password, check_hash_pass, verify_hash_pass


@staticmethod
def select_users():
    with session_factory() as session:
        query = (
            select(User)
            .limit(50)
        )
        id = session.execute(query).scalar().all()
        res = session.execute(query)
        result_orm = res.scalars().all()
        result_dto = [UserDTO.model_validate(row, from_attributes=True) for row in result_orm]
        return result_dto

@staticmethod
def get_user_id(email_: str):
    with session_factory() as session:
        query = (
            select(User.id).filter(User.email == email_)
        )
        return session.execute(query).scalar_one()

@staticmethod
def insert_item(title_: str, description_: str, price_: int, city_: str, user_id_: int):
    item_car = Items(title=title_, description=description_, price=price_, city=city_, user_id=user_id_)
    with session_factory() as session:
        session.add(item_car)
        session.commit()
    return {"msg", f"item {title_} added"}



@staticmethod
# Need insert password (hash)
def insert_user(_username: str, _password: str, _name: str, _surname: str, _email: str, _city: str, _phone: str):
    hash_pass_ = hash_password(_password)
    new_user = User(name=_name, surname=_surname, email=_email, city=_city, phone=_phone, username=_username, hash_pass=hash_pass_)
    with session_factory() as session:
        session.add(new_user)
        session.commit()



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
def check_hash(email_: str, password_: str):
    with session_factory() as session:
        query = (
            select(User.hash_pass).filter(User.email == email_)
        )
        hash_storage = session.execute(query).scalar_one()
        return verify_hash_pass(password_, hash_storage)
