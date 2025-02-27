from ..data_models.models import User
from ..security.hash_pass import verify_hash_pass
from sqlalchemy import select
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

class AuthRepository:
    @classmethod
    async def authentication(cls, data: dict, session: AsyncSession):
        user = User(**data)
        query = (select(User.hash_pass).filter(User.email == user.email))
        hash_storage = (await session.execute(query)).scalar_one_or_none()
        if not hash_storage:
            return HTTPException(status_code=401, detail="Incorrect password or email")
        return await verify_hash_pass(user.hash_pass, hash_storage)
