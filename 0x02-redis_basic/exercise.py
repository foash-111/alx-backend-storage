#!/usr/bin/env python3
"""redis with python as simple cache"""


import redis
from uuid import uuid4
from typing import Union, Optional, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """decorator"""
    @wraps(method)
    def wrapper(*args, **kwargs):
        r = redis.Redis()
        r.incr(method.__qualname__)
        return method(*args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """decorator"""
    @wraps(method)
    def wrapper(*args, **kwargs):
        r = redis.Redis()
        output = method(*args, **kwargs)
        r.rpush(f'{method.__qualname__}:inputs', str(args[1:]))
        # [1:] to skip the first parameter that passed which is 'self'
        r.rpush(f'{method.__qualname__}:outputs', output)
        return output
    return wrapper


class Cache:
    """base class"""
    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float, None]) -> str:
        id = str(uuid4())
        self._redis.set(id, data)
        return id

    def get(self, key: str, fn: Optional[Callable] = None) ->\
            Union[bytes, int, str, float]:
        """like redis get but return the value like we store it"""
        value = self._redis.get(key)
        if value is None:
            return None
        elif fn is None:
            return value
        else:
            converted_value = fn(value)
        return converted_value

    def get_str(self, value: bytes) -> str:
        return str(value)

    def get_int(self, value: bytes) -> int:
        try:
            return int(value)
        except ValueError:
            raise ValueError("can't convert into integer")
