from fastapi import APIRouter, Response, HTTPException

from ..queries.orm import check_hash, get_user_id
from ..security.security_config import config, security

auth_router = APIRouter(
    prefix="/authentication"
)

@auth_router.post("/check_user")
async def check_pass(email_: str, pass_: str, response: Response):
    if check_hash(email_, pass_):
        uid_ = await get_user_id(email_)
        token = security.create_access_token(uid=str(uid_))
        response.set_cookie(config.JWT_ACCESS_COOKIE_NAME, token)
        return {"access_token", token}
    raise HTTPException(status_code=401, detail="Incorrect password or email")
