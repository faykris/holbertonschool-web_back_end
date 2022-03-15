#!/usr/bin/env python3
"""
0. Writing strings to Redis
"""
import redis
from uuid import uuid4
from typing import Union, Callable, Optional
from functools import wraps


def replay(fn: Callable) -> None:
    r = redis.Redis()
    f_name = fn.__qualname__
    n_calls = r.get(f_name)
    try:
        n_calls = n_calls.decode("utf-8")
    except Exception:
        n_calls = 0
    print(f"{f_name} was called {n_calls} times:")

    inputs = r.lrange(f_name + ":inputs", 0, -1)
    outputs = r.lrange(f_name + ":outputs", 0, -1)

    for inp, out in zip(inputs, outputs):
        try:
            inp = inp.decode("utf-8")
        except Exception:
            inp = ""
        try:
            out = out.decode("utf-8")
        except Exception:
            out = ""
        print(f"{f_name}(*{inp}) -> {out}")


def call_history(method: Callable) -> Callable:
    """call_history - history wrap method"""

    @wraps(method)
    def wrapper(self, *args, **kwds):
        """wrapper"""
        i_args = str(args)
        self._redis.rpush(f"{method.__qualname__}:inputs", i_args)
        o_args = str(method(self, *args, **kwds))
        self._redis.rpush(f"{method.__qualname__}:outputs", o_args)
        return o_args

    return wrapper


def count_calls(method: Callable) -> Callable:
    """count_calls - counter wrap method"""
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwds):
        """wrapper"""
        self._redis.incr(key)
        return method(self, *args, **kwds)
    return wrapper


class Cache:
    """Cache - class"""

    def __init__(self):
        """Constructor method"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """store - method"""
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
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
