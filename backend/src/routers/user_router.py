from fastapi import APIRouter

from ..queries.orm import select_users, async_select_user


user_router = APIRouter(
    prefix="/user"
)

@user_router.get("/all")
async def get_all_users():
    return await async_select_user()
