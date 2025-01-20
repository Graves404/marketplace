from .models import UpdateUser

class Validation:
    @classmethod
    def validation_data(cls, _username: str, _name: str, _surname: str, _email: str, _city: str, _phone: str):
        user = UpdateUser()
        if _username is not None:
            user.username = _username
        if _name is not None:
            user.name = _name
        if _surname is not None:
            user.surname = _surname
        if _email is not None:
            user.email = _email
        if _city is not None:
            user.city = _city
        if _phone is not None:
            user.phone = _phone

        return user
