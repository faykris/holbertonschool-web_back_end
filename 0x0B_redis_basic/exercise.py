#!/usr/bin/env python3
"""
0. Writing strings to Redis
"""
from itertools import count
import redis
from uuid import uuid4
from typing import Union, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """count_calls - counter wrap method"""
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, name):
        """wrapper"""
        print(key)
        print(name)
    return wrapper


class Cache:
    """Cache - class"""

    def __init__(self):
        """Constructor method"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """store - method"""
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable) -> Union[str, bytes, int, float]:
        """get - method"""
        if fn:
            return fn(self._redis.get(key))
        return self._redis.get(key)

    def get_str(self, key: str) -> str:
        """get_str"""
        return str(key)

    def get_int(self, key: str) -> int:
        """get_str"""
        return int(key)
