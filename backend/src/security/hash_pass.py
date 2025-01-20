from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError

def hash_password(pass_: str):
    ph = PasswordHasher()
    hash_pass = ph.hash(pass_)
    return hash_pass

async def verify_hash_pass(input_password_: str, stored_hash_: str):
    ph = PasswordHasher()
    try:
        return ph.verify(stored_hash_, input_password_)
    except VerifyMismatchError:
        return False
    