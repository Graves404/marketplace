from src.models import User, Items
from sqlalchemy import select
from src.database import engine, session

@staticmethod
def select_users():
    with session() as session_factory:
        query = select(User)
        result = session_factory.execute(query)
        users = result.all()
        
def insert_item(name : str):
    item_car = Items(id = 1, title=name, description = "New Auto", price = 1000, city = "Kapan", id_user = 1)
    with session() as session_factory:
        session_factory.add(item_car)
        session_factory.commit()


