from .models import User
from ..pydantic_schemas.schemas import UserUpdatePostDTO

class Validation:
    @classmethod
    def validation_data(cls, user: User, user_update: UserUpdatePostDTO):
        temp_user = user
        if user_update.username is not None and len(user_update.username) != 0:
            temp_user.username = user_update.username
        if user_update.name is not None and len(user_update.name) != 0:
            temp_user.name = user_update.name
        if user_update.surname is not None and len(user_update.surname) != 0:
            temp_user.surname = user_update.surname
        if user_update.email is not None and len(user_update.email) != 0:
            temp_user.email = user_update.email
        if user_update.city is not None and len(user_update.city) != 0:
            temp_user.city = user_update.city
        if user_update.phone is not None and len(user_update.phone) != 0:
            temp_user.phone = user_update.phone

        return temp_user
