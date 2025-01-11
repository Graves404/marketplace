from fastapi import FastAPI
from queries.orm import select_users, select_user_by_id, insert_user
from schemas import UserDTO
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = [
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/all_users")
def get_users() -> list[UserDTO]:
    users = select_users()
    return users

@app.get("/get_user_by_id")
def get_user_by_id(id_: int):
    user = select_user_by_id(id_)
    return user

@app.post("/insert_user")
def insert_user_fast_api(name_: str, surname_: str, email_: str, city_: str, phone_: str):
    insert_user(name_, surname_, email_, city_, phone_)
    return {
            "ok": "True",
            "msg": "Added the new user"
            }
