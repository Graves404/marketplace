from fastapi import Request, UploadFile, HTTPException
from ..queries.item_repository import ItemRepository
from ..security.security_config import config
from ..google_cloud.cloud_settings import upload_file
import jwt
class Item:
    @classmethod
    async def add_new_item(cls, req: Request, title_: str, description_: str, price_: int, city_: str, files: list[UploadFile]):
        token = req.cookies.get("mne_market_accesses_token")
        jwt_decode = jwt.decode(token, config.JWT_SECRET_KEY, config.JWT_ALGORITHM)
        user_id = int(jwt_decode["sub"])
        if user_id is not None:
            url_file = upload_file(files)
            return await ItemRepository.add_new_item(title_, description_, price_, city_, user_id, url_file)
        raise HTTPException(status_code=403, detail="Incorrect password or email")
