from argon2 import PasswordHasher


def hash_password(pass_: str):
    ph = PasswordHasher()
    hash_pass = ph.hash(pass_)
    return hash_pass

def check_hash_pass(pass_hash_: str):
    ph = PasswordHasher()
    return ph.check_needs_rehash(pass_hash_)

def verify_hash_pass(input_password_: str, stored_hash_: str):
    ph = PasswordHasher()
    try:
        return ph.verify(stored_hash_, input_password_)
    except:
        return False
