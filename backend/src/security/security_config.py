from authx import AuthX, AuthXConfig
from ..settings.config import settings

config = AuthXConfig()
config.JWT_SECRET_KEY = settings.JWT_SECRET_KEY
config.JWT_TOKEN_LOCATION = ["headers", "cookies"]
config.JWT_HEADER_NAME = "Authorization"
config.JWT_HEADER_TYPE = "Bearer"
config.JWT_COOKIE_CSRF_PROTECT = False
config.JWT_ALGORITHM = "HS256"

# config.JWT_ACCESS_TOKEN_EXPIRES = 900
# config.JWT_REFRESH_TOKEN_EXPIRES = 604800

security = AuthX(config=config)
