from fastapi import APIRouter, Depends, Request, UploadFile, BackgroundTasks, File, Form
from ..security.security_config import security
from ..service.items_service import Item
from sqlalchemy.ext.asyncio import AsyncSession
from ..engine_database.database import get_async_session_factory
from ..pydantic_schemas.schemas import ItemsPostDTO, PaymentItemDTO
from async_lru import alru_cache
from ..payments.stripe_config import StripeConfig

item_router = APIRouter(
    prefix="/items"
)

@alru_cache()
@item_router.get("/all_items")
async def get_all(session: AsyncSession = Depends(get_async_session_factory)):
    return await Item.get_all_items(session)

@item_router.post("/add_item", dependencies=[Depends(security.access_token_required)])
async def add_new_item_service(req: Request, bg: BackgroundTasks, title: str = Form(...), description: str = Form(...),
                               price: int = Form(...), city: str = Form(...), files: list[UploadFile] = File(...),
                               session: AsyncSession = Depends(get_async_session_factory)):
    item = ItemsPostDTO(title=title, description=description, price=price, city=city)
    return await Item.add_new_item(req, bg, item, files, session)

@alru_cache()
@item_router.get("/get_item/{id}")
async def get_current_item(id_: int, session: AsyncSession = Depends(get_async_session_factory)):
    return await Item.get_current_item(id_, session)

@item_router.post("/delete_item/{item}", dependencies=[Depends(security.access_token_required)])
async def delete_item(id_: int, urls_: list[str], session: AsyncSession = Depends(get_async_session_factory)):
    return await Item.delete_item(id_, urls_, session)


@item_router.post("/payment_item_session")
async def buy_item_by_id(payment: PaymentItemDTO):
    return await StripeConfig.create_payment_session(payment)