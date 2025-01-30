from fastapi import Response, HTTPException
from ..queries.auth_repository import AuthRepository
from ..security.security_config import config, security
from .user_service import User
from sqlalchemy.ext.asyncio import AsyncSession
from ..pydantic_schemas.schemas import UserAuthenticationDTO


class Auth:
    @classmethod
    async def authentication(cls, user: UserAuthenticationDTO, response: Response, session: AsyncSession):

        data = user.model_dump()
        if await AuthRepository.authentication(data, session=session):
            uid_ = await User.get_id_current_user(email_=user.email, session=session)
            token = security.create_access_token(uid=str(uid_))
            response.set_cookie(config.JWT_ACCESS_COOKIE_NAME, token)
            return token
        raise HTTPException(status_code=401, detail="Incorrect password or email")
