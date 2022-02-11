#!/usr/bin/env python3
"""5. Encrypting passwords"""
import bcrypt


def hash_password(password: str) -> bytes:
    """hash_password - returns hashed password in byte string"""
    return bcrypt.hashpw(password.encode("UTF-8"), bcrypt.gensalt())
