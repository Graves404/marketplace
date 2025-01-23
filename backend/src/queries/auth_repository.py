from ..data_models.models import User
from ..engine_database.database import (async_session_factory)
from ..security.hash_pass import verify_hash_pass
from sqlalchemy import select
from fastapi import HTTPException

class AuthRepository:
    @classmethod
    async def authentication(cls, email_: str, password_: str):
        async with async_session_factory() as session:
            query = (
                select(User.hash_pass).filter(User.email == email_)
            )
            hash_storage = (await session.execute(query)).scalar_one_or_none()
            if not hash_storage:
                return HTTPException(status_code=401, detail="Incorrect password or email")

            return await verify_hash_pass(password_, hash_storage)

#TODO Change all session