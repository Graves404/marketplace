from fastapi import Response, HTTPException
from ..queries.auth_repository import AuthRepository
from ..security.security_config import config, security
from .user_service import User
from sqlalchemy.ext.asyncio import AsyncSession


class Auth:
    @classmethod
    async def authentication(cls, email_: str, password_: str, response: Response, session: AsyncSession):
        if await AuthRepository.authentication(email_=email_, password_=password_, session=session):
            uid_ = await User.get_id_current_user(email_=email_, session=session)
            token = security.create_access_token(uid=str(uid_))
            response.set_cookie(config.JWT_ACCESS_COOKIE_NAME, token)
            return token
        raise HTTPException(status_code=401, detail="Incorrect password or email")
