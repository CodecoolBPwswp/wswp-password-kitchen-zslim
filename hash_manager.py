import bcrypt


def hash_password(plain_text_password):
    hashed_password = bcrypt.hashpw(plain_text_password.encode("utf-8"), bcrypt.gensalt())
    return hashed_password.decode("utf-8")


def verify_password(given_plain_text, hashed_password):
    is_correct = bcrypt.checkpw(given_plain_text.encode("utf-8"), hashed_password.encode("utf-8"))
    return is_correct
