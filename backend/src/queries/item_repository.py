from ..database import async_session_factory
from ..data_models.models import Items, Images
from sqlalchemy import select
from sqlalchemy.orm import selectinload, joinedload
class ItemRepository:
    @classmethod
    async def get_all(cls):
        async with async_session_factory() as session:
            query = (select(Items).options(selectinload(Items.images)))
            start_query = await session.execute(query)
            result = start_query.scalars().all()
            return result

    @classmethod
    async def add_new_item(cls, title_: str, description_: str, price_: int, city_: str, user_id_: int, url_files_: list[str]):
        item = Items(title=title_, description=description_, price=price_, city=city_, user_id=user_id_)
        async with async_session_factory() as session:
            try:
                session.add(item)
                await session.flush()
                images = [Images(url_photo=url, item_id=item.id) for url in url_files_]
                session.add_all(images)
                await session.commit()
                return {"msg", f"item {title_} added and photo {len(url_files_)}"}
            except Exception as e:
                await session.rollback()
                raise e
# TODO:
#  1. Add Function "Update" and "Delete" of item, if user wanna change any information about self item or delete current item.
#  Use SQLAlchemy methods: 1. Update 2. Delete
#  Link: https://docs.sqlalchemy.org/en/20/core/dml.html