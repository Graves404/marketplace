from fastapi import FastAPI
from queries.orm import select_users, select_user_by_id
from schemas import UserDTO


app = FastAPI()
@app.get("/all_users")
def get_users() -> list[UserDTO]:
    users = select_users()
    return users

@app.get("/get_user_by_id")
def get_user_by_id(id_: int):
    user = select_user_by_id(id_)
    return user