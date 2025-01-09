from src.models import User, Items
from sqlalchemy import select
from src.database import engine, session_factory

@staticmethod
def select_users():
    with session_factory() as session:
        query = select(User)
        result = session.execute(query)
        users = result.all()

@staticmethod
def insert_item(name : str):
    item_car = Items(title=name, description = "New Auto", price = 1000, city = "Kapan", user_id = 1)
    with session_factory() as session:
        session.add(item_car)
        session.commit()

@staticmethod
def insert_user(_name : str, _surname : str):
    new_user = User(name = _name, surname = _surname)
    with session_factory() as session:
        session.add(new_user)
        session.commit()

@staticmethod
def select_user_by_city(_city : str):
    with session_factory() as session:
        query = (
                select(
                    User.id,
                    User.name,
                    User.surname,
                    User.email
                    ).select_from(User).filter(
                        User.city.contains(_city)
                        )
                )
        result = session.execute(query)
        users = result.all()
        print(users)
