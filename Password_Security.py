from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError, VerificationError, InvalidHashError
ph = PasswordHasher()
def hash_password(password):
    return ph.hash(password)
def verify_password(stored_hash, entered_password):
    try:
        return ph.verify(stored_hash, entered_password)
    except (VerifyMismatchError, VerificationError, InvalidHashError):
        return False