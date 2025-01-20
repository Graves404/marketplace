from fastapi import Request, UploadFile, HTTPException
from ..queries.item_repository import ItemRepository
from ..google_cloud.cloud_settings import upload_file, delete_files
from ..service.jwt_service import JwtService
from ..pydantic_schemas.schemas import ItemIMageRelDTO

class Item:
    @classmethod
    async def get_all_items(cls):
        result_orm = await ItemRepository.get_all()
        result_dto = [ItemIMageRelDTO.model_validate(row, from_attributes=True) for row in result_orm]
        return result_dto
    @classmethod
    async def add_new_item(cls, req: Request, title_: str, description_: str, price_: int, city_: str, files: list[UploadFile]):
        token = req.cookies.get("mne_market_accesses_token")
        user_id = JwtService.get_id_user_token(token)
        if user_id is not None:
            url_file = upload_file(files)
            return await ItemRepository.add_new_item(title_, description_, price_, city_, user_id, url_file)
        raise HTTPException(status_code=403, detail="Incorrect password or email")

    @classmethod
    async def delete_item(cls, id_: int, urls: list[str]):
        print(f"id {id_}")
        print(f"urls {urls}")
        data = delete_files(urls)   # delete from cloud storage
        return {"msg": f"{data}"}


# TODO: add more function:
#  1. update_item (title, description, price, city)
#  2. Delete item from DB.