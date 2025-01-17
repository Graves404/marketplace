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

class UserPassDTO(UserDTO):
    hash_pass: str

class ItemsPostDTO(BaseModel):
    title: str
    description: str
    price: int
    city: str
    user_id: int

class ItemDTO(ItemsPostDTO):
    id: int

class ItemRelDTO(ItemDTO):
    user: "UserDTO"

class UserRelDTO(UserDTO):
    items: list["ItemDTO"]


class PasswordPostDTO(BaseModel):
    hash_pass: str

class PasswordDTO(PasswordPostDTO):
    id: int

class PasswordRelDTO(PasswordDTO):
    user: "UserDTO"


class ImagePostDTO(BaseModel):
    file_name: str
    url_photo: str
    items_id: int


class ImageDTO(ImagePostDTO):
    id: int

class ImageReDTO(ImageDTO):
    items: "ItemDTO"
