from fastapi import UploadFile

from ..database import async_session_factory
from ..data_models.models import Items, Images
from sqlalchemy import select, delete
from sqlalchemy.orm import selectinload
from ..settings.config import settings
class ItemRepository:
    @classmethod
    async def get_all(cls):
        async with async_session_factory() as session:
            query = (select(Items).options(selectinload(Items.images)))
            start_query = await session.execute(query)
            result = start_query.scalars().all()
            return result

    @classmethod
    async def add_new_item(cls, title_: str, description_: str, price_: int, city_: str, user_id_: int, files: list[UploadFile]):
        item = Items(title=title_, description=description_, price=price_, city=city_, user_id=user_id_)
        async with async_session_factory() as session:
            try:
                session.add(item)
                await session.flush()
                images = [Images(url_photo=settings.URL_CLOUD_STORAGE+file.filename, item_id=item.id) for file in files]
                session.add_all(images)
                await session.commit()
                return {"msg", f"item {title_} added and photo {len(files)}"}
            except Exception as e:
                await session.rollback()
                raise e

    @classmethod
    async def delete_item(cls, id_item: int):
        async with async_session_factory() as session:
            if id_item is not None:
                query = (delete(Items).filter(Items.id == id_item))
                await session.execute(query)
                await session.commit()
            return {"msg": f"Item {id_item} deleted"}


    #TODO UPDATE ITEM (METHOD)

    @classmethod
    async def get_item_by_id(cls, id_: int):
        async with async_session_factory() as session:
            query = (select(Items).filter(Items.id == id_).options(selectinload(Items.images)))
            result_query = await session.execute(query)
            result_orm = result_query.scalars().all()
            return result_orm
