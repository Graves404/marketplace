from fastapi import APIRouter, Depends, Request, HTTPException
from ..security.security_config import security, config
from ..queries.orm import insert_item
import jwt

item_router = APIRouter(
    prefix="/items"
)

@item_router.post("/add_item", dependencies=[Depends(security.access_token_required)])
async def insert_item_to_db(req: Request, title_: str, description_: str, price_: int, city_: str):
    token = req.cookies.get("mne_market_accesses_token")
    jwt_decode = jwt.decode(token, config.JWT_SECRET_KEY, config.JWT_ALGORITHM)
    user_id = int(jwt_decode["sub"])
    if user_id is not None:
        return insert_item(title_, description_, price_, city_, user_id)
    raise HTTPException(status_code=403, detail="Incorrect password or email")

