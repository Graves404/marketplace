from fastapi import FastAPI, HTTPException, Response, Depends, Request
from queries.orm import select_users, get_user_id, insert_user, get_user_by_username, check_hash, insert_item
from schemas import UserDTO
from fastapi.middleware.cors import CORSMiddleware
from authx import AuthX, AuthXConfig
import jwt

app = FastAPI()

config = AuthXConfig()
config.JWT_SECRET_KEY = "c4380a77d14d770c8785d270d50d2eb2a1486f85201646daab235d2ba8600b65"
config.JWT_ACCESS_COOKIE_NAME = "mne_market_accesses_token"
config.JWT_TOKEN_LOCATION = ["cookies"]

security = AuthX(config=config)

origins = [
    "http://localhost:5173",
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/all_users")
async def get_users() -> list[UserDTO]:
    users = select_users()
    return users

@app.get("/get_user_id")
async def get_user_by_id(email_: str):
    user = get_user_id(email_)
    return user

@app.post("/insert_user")
async def insert_user_fast_api(username_: str, password_: str, name_: str, surname_: str, email_: str, city_: str, phone_: str):
    insert_user(username_, password_, name_, surname_, email_, city_, phone_)
    return {
            "ok": "True",
            "msg": "Added the new user"
            }

@app.get("/user/", tags=['user'])
async def read_user(username_: str):
    user = get_user_by_username(username_)
    return user

@app.post("/hash_pass")
async def check_pass(email_: str, pass_: str, response: Response):
    if check_hash(email_, pass_):
        uid_ = await get_user_by_id(email_)
        token = security.create_access_token(uid=str(uid_))
        response.set_cookie(config.JWT_ACCESS_COOKIE_NAME, token)
        return {"access_token", token}
    raise HTTPException(status_code=401, detail="Incorrect password or email")

@app.get("/add_new_item", dependencies=[Depends(security.access_token_required)])
async def insert_item_to_db(req: Request, title_: str, description_: str, price_: int, city_: str):
    token = req.cookies.get("mne_market_accesses_token")
    jwt_decode = jwt.decode(token, config.JWT_SECRET_KEY, config.JWT_ALGORITHM)
    user_id = int(jwt_decode["sub"])
    if user_id is not None:
        return insert_item(title_, description_, price_, city_, user_id)
    raise HTTPException(status_code=403, detail="Incorrect password or email")
