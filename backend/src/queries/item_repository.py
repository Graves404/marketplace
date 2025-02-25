from fastapi import UploadFile
from ..data_models.models import Items, Images
from sqlalchemy import select, delete
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession
from ..settings.config import settings

class ItemRepository:
    
    @classmethod
    async def get_all(cls, session: AsyncSession):
        query = (select(Items).options(selectinload(Items.images)))
        start_query = await session.execute(query)
        return start_query.scalars().all()
    
    @classmethod
    async def add_new_item(cls, data: dict, user_id_: int, files: list[UploadFile],
                           session: AsyncSession):
        item = Items(**data)
        item.user_id = user_id_
        try:
            session.add(item)
            await session.flush()
            images = [Images(url_photo=settings.URL_CLOUD_STORAGE + file.filename, item_id=item.id) for file in files]
            session.add_all(images)
            await session.commit()
            return {"code": 201, "msg": f"The item was added and photo {len(files)}"}
        except Exception as e:
            await session.rollback()
            raise e

    @classmethod
    async def delete_item(cls, id_item: int, session: AsyncSession):
        if id_item is not None:
            query = (delete(Items).filter(Items.id == id_item))
            await session.execute(query)
            await session.commit()
            return {"code": 200, "msg": f"The item {id_item} was deleted"}
        else:
            return {"code": 404, "msg": "The item was not found"}


    #TODO UPDATE ITEM (METHOD)

    @classmethod
    async def get_item_by_id(cls, id_: int, session: AsyncSession):
        try:
            query = (select(Items).filter(Items.id == id_).options(selectinload(Items.user), selectinload(Items.images)))
            result_query = await session.execute(query)
            return result_query.scalars().first()
        except:
            return {"code": 404, "msg": "The item was not found"}
