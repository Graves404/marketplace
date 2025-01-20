from fastapi import APIRouter, Response
from ..service.auth_service import Auth

auth_router = APIRouter(
    prefix="/authentication"
)

@auth_router.post("/check_user")
async def check_pass(email_: str, pass_: str, response: Response):
    return await Auth.authentication(email_, pass_, response)

