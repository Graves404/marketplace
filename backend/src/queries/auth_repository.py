from ..data_models.models import User
from ..database import async_session_factory
from ..security.hash_pass import verify_hash_pass
from sqlalchemy import select

class AuthRepository:
    @classmethod
    async def authentication(cls, email_: str, password_: str):
        async with async_session_factory() as session:
            query = (
                select(User.hash_pass).filter(User.email == email_)
            )
            hash_storage = session.execute(query).scalar_one()
            return await verify_hash_pass(password_, hash_storage)
