from ..database import async_session_factory
from ..data_models.models import Items, Images
class ItemRepository:
    @classmethod
    async def add_new_item(cls, title_: str, description_: str, price_: int, city_: str, user_id_: int, url_files_: list[str]):
        item = Items(title=title_, description=description_, price=price_, city=city_, user_id=user_id_)
        async with async_session_factory() as session:
            try:
                session.add(item)
                await session.flush()
                print(f"Items id {item.id}")
                images = [Images(url_photo=url, items_id=item.id) for url in url_files_]
                session.add_all(images)
                await session.commit()
                return {"msg", f"item {title_} added and photo {len(url_files_)}"}
            except Exception as e:
                await session.rollback()
                raise e
