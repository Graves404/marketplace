from fastapi import APIRouter, Response, Depends
from ..service.auth_service import Auth
from sqlalchemy.ext.asyncio import AsyncSession
from ..engine_database.database import get_async_session_factory

auth_router = APIRouter(
    prefix="/authentication"
)

@auth_router.post("/check_user")
async def check_pass(email_: str, pass_: str, response: Response, session: AsyncSession = Depends(get_async_session_factory)):
    return await Auth.authentication(email_=email_, password_=pass_, response=response, session=session)

