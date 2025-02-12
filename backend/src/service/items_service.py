from fastapi import Request, UploadFile, HTTPException, BackgroundTasks
from ..queries.item_repository import ItemRepository
from ..google_cloud.cloud_settings import upload_file, delete_files
from ..service.jwt_service import JwtService
from ..pydantic_schemas.schemas import ItemIMageRelDTO, ItemGeneralDTO
from ..pydantic_schemas.schemas import ItemsPostDTO
from sqlalchemy.ext.asyncio import AsyncSession

class Item:
    @classmethod
    async def get_all_items(cls, session: AsyncSession) -> list[ItemIMageRelDTO]:
        result_orm = await ItemRepository.get_all(session)
        result_dto = [ItemGeneralDTO.model_validate(row, from_attributes=True) for row in result_orm]
        return result_dto
    @classmethod
    async def add_new_item(cls, req: Request, bg: BackgroundTasks, item: ItemsPostDTO, files: list[UploadFile], session: AsyncSession):
        token = req.headers.get("Authorization")
        user_id = JwtService.get_id_user_token(token)
        data = item.model_dump()
        if user_id is not None:
            for file in files:
                file_content = await file.read()
                bg.add_task(upload_file, file.filename, file_content, file.content_type)
            #TODO: Sometimes item can be without images. If user don't upload image - we can get Expectation
            return await ItemRepository.add_new_item(data, user_id, files, session)
        raise HTTPException(status_code=403, detail="Incorrect password or email")

    @classmethod
    async def test_upload_background(cls, files: list[UploadFile], bg: BackgroundTasks):
        for file in files:
            file_content = await file.read()
            bg.add_task(upload_file, file.filename, file_content, file.content_type)

    @classmethod
    async def delete_item(cls, id_: int, urls: list[str], session: AsyncSession):
        delete_files(urls)  # delete from cloud storage
        response = await ItemRepository.delete_item(id_, session)
        return {"msg": f"{response}"}

    #TODO: UPDATE ITEM METHOD

    @classmethod
    async def get_current_item(cls, id_: int, session: AsyncSession):
        item = await ItemRepository.get_item_by_id(id_, session)
        result_dto = ItemIMageRelDTO.model_validate(item, from_attributes=True)
        return result_dto


    @classmethod
    async def validate_data_for_buy(cls):
        return await ...


