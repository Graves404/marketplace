from pydantic import BaseModel, EmailStr

class UserPostDTO(BaseModel):
    name: str
    surname: str
    email: EmailStr
    city: str
    phone: str
    username: str
class UserDTO(UserPostDTO):
    id: int

class ItemsPostDTO(BaseModel):
    title: str
    description: str
    price: int
    city: str
    user_id: int

class ItemDTO(ItemsPostDTO):
    id: int


class ImagePostDTO(BaseModel):
    url_photo: str
    item_id: int


class ImageDTO(ImagePostDTO):
    id: int

class UserRelDTO(UserDTO):
    items: list["ItemDTO"]


class ItemIMageRelDTO(ItemDTO):
    images: list["ImageDTO"]

class ItemRelDTO(ItemDTO):
    user: "UserDTO"

class ImageReDTO(ImageDTO):
    items: "ItemDTO"