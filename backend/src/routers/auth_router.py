from fastapi import APIRouter, Response, Depends
from ..service.auth_service import Auth
from sqlalchemy.ext.asyncio import AsyncSession
from ..engine_database.database import get_async_session_factory
from ..pydantic_schemas.schemas import UserAuthenticationDTO

auth_router = APIRouter(
    prefix="/authentication"
)

@auth_router.post("/check_user")
async def check_pass(user: UserAuthenticationDTO, response: Response, session: AsyncSession = Depends(get_async_session_factory)):
    return await Auth.authentication(user, response=response, session=session)

