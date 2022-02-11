#!/usr/bin/env python3
"""5. Encrypting passwords"""
import bcrypt


def hash_password(password: str) -> bytes:
    """hash_password - returns hashed password in byte string"""
    return bcrypt.hashpw(password.encode("UTF-8"), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """is valid - verify if a password match with hashed"""
    return bcrypt.checkpw(password.encode('UTF-8'), hashed_password)
