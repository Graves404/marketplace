from fastapi import APIRouter, Depends, Request, HTTPException, UploadFile
from ..security.security_config import security, config
from ..queries.orm import insert_item
from ..google_cloud.cloud_settings import upload_file
import jwt

item_router = APIRouter(
    prefix="/items"
)

@item_router.post("/add_item", dependencies=[Depends(security.access_token_required)])
async def insert_item_to_db(req: Request, title_: str, description_: str, price_: int, city_: str, file_: UploadFile):
    token = req.cookies.get("mne_market_accesses_token")
    jwt_decode = jwt.decode(token, config.JWT_SECRET_KEY, config.JWT_ALGORITHM)
    user_id = int(jwt_decode["sub"])
    if user_id is not None:
        url_file = upload_file(file_.filename, file_)
        return insert_item(title_, description_, price_, city_, user_id, file_.filename, url_file)
    raise HTTPException(status_code=403, detail="Incorrect password or email")

@item_router.post("/upload_file", dependencies=[Depends(security.access_token_required)])
async def create_upload_file(file: UploadFile):
    return upload_file(file.filename, file)

