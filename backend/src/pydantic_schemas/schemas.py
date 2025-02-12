from pydantic import BaseModel, EmailStr, field_validator

class UserUpdatePasswordDTO(BaseModel):
    email: EmailStr
    hash_pass: str
    new_pass: str
class UserAuthenticationDTO(BaseModel):
    email: EmailStr
    hash_pass: str
class UserPostDTO(BaseModel):
    name: str
    surname: str
    email: EmailStr
    city: str
    phone: str
    username: str

class EmailRabbitSchemas(BaseModel):
    email: EmailStr
    subject: str
    message: str

class UserRegistrationDTO(UserPostDTO):
    hash_pass: str

class PaymentItemDTO(BaseModel):
    title: str
    description: str
    price: int

class UserDTO(UserPostDTO):
    id: int


class UserUpdatePostDTO(UserPostDTO):
    name: str | None
    surname: str | None
    email: EmailStr | None
    city: str | None
    phone: str | None
    username: str | None

    @field_validator("email", mode='before')
    def validate_email(cls, value):
        if value == "":
            return None
        return value


class ItemsPostDTO(BaseModel):
    title: str
    description: str
    price: int
    city: str

class ItemDTO(ItemsPostDTO):
    id: int
    user_id: int

class ItemGeneralDTO(ItemDTO):
    images: list["ImageDTO"]


class ImagePostDTO(BaseModel):
    url_photo: str
    item_id: int


class ImageDTO(ImagePostDTO):
    id: int

class UserRelDTO(UserDTO):
    items: list["ItemDTO"]

class ItemRelDTO(ItemDTO):
    user: "UserDTO"


class ItemIMageRelDTO(ItemRelDTO):
    images: list["ImageDTO"]


class ImageReDTO(ImageDTO):
    items: "ItemDTO"

# TODO 1. Change some models for response endpoint, some models return more information than needs
#  Example: In methods "get_all_items" we use model ItemIMageRelDTO and we don't need information about user, but in
#  method "get_current_item_by_id" frontend renders some user detail: Name, Phone, Email