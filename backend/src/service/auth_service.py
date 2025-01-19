from fastapi import Response, HTTPException
from ..queries.auth_repository import AuthRepository
from ..security.security_config import config, security
from .user_service import User

class Auth:
    @classmethod
    async def authentication(cls, email_: str, password_: str, response: Response):
        if AuthRepository.authentication(email_, password_):
            uid_ = await User.get_id_current_user(email_)
            token = security.create_access_token(uid=str(uid_))
            response.set_cookie(config.JWT_ACCESS_COOKIE_NAME, token)
            return {"access_token", token}
        raise HTTPException(status_code=401, detail="Incorrect password or email")
