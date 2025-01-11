from models import User, Items
from sqlalchemy import select
from database import engine, session_factory
from schemas import UserDTO, UserRelDTO
from sqlalchemy.orm import relationship, selectinload


@staticmethod
def select_users():
    with session_factory() as session:
        query = (
            select(User)
            .limit(50)
        )
        res = session.execute(query)
        result_orm = res.scalars().all()
        result_dto = [UserDTO.model_validate(row, from_attributes=True) for row in result_orm]
        return result_dto

@staticmethod
def select_user_by_id(id_: int):
    with session_factory() as session:
        query = (
            select(User).filter(User.id == id_).options(selectinload(User.items))
        )
        res = session.execute(query)
        result_orm = res.scalars().all()
        session.query(User).get(id_)
        result_dto = [UserRelDTO.model_validate(row, from_attributes=True) for row in result_orm]
        return result_dto

@staticmethod
def insert_item(name: str):
    item_car = Items(title=name, description="Good choose", price=700, city="Donghu", user_id=4)
    with session_factory() as session:
        session.add(item_car)
        session.commit()


@staticmethod
def insert_user(_name: str, _surname: str):
    new_user = User(name=_name, surname=_surname)
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
