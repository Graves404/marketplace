import jwt
from ..security.security_config import config

class JwtService:
    @classmethod
    def get_id_user_token(cls, token: str) -> int:
        jwt_decode = jwt.decode(token, config.JWT_SECRET_KEY, config.JWT_ALGORITHM)
        user_id = int(jwt_decode["sub"])
        return user_id
