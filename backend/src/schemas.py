from pydantic import BaseModel, EmailStr

class UserPostDTO(BaseModel):
    name: str
    surname: str
    email: EmailStr
    city: str
    phone: str
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

class ItemRelDTO(ItemDTO):
    user: "UserDTO"

class UserRelDTO(UserDTO):
    items: list["ItemDTO"]
