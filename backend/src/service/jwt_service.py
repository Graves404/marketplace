import jwt
from ..security.security_config import config

class JwtService:

    @classmethod
    def extract_token(cls, token: str) -> str:
        if token.startswith("Bearer "):
            return token[len("Bearer "):]
        return token

    @classmethod
    def get_id_user_token(cls, token: str) -> int:
        clean_token = cls.extract_token(token)
        jwt_decode = jwt.decode(clean_token, config.JWT_SECRET_KEY, config.JWT_ALGORITHM)
        user_id = int(jwt_decode["sub"])
        return user_id
