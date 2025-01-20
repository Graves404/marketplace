from fastapi import APIRouter, Depends, Request, UploadFile
from ..security.security_config import security
from ..service.items_service import Item


item_router = APIRouter(
    prefix="/items"
)

@item_router.get("/all_items")
async def get_all():
    return await Item.get_all_items()

@item_router.post("/add_item", dependencies=[Depends(security.access_token_required)])
async def add_new_item_service(req: Request, title_: str, description_: str, price_: int, city_: str, files: list[UploadFile]):
    return await Item.add_new_item(req, title_, description_, price_, city_, files)

@item_router.post("/delete_item/{item}", dependencies=[Depends(security.access_token_required)])
async def delete_item(req: Request, id_: int, urls_: list[str]):
    return await Item.delete_item(id_, urls_)