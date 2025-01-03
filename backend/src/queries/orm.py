from src.models import User
from sqlalchemy import select
from src.database import engine 

def fetch_all_users():
    with engine.connect() as conn:
        res = conn.execute(select(User)).all()
        print(res)


def insert_user(user : str):
    print(f'i inserted user {user}')



