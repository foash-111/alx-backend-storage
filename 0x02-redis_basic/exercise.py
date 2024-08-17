#!/usr/bin/env python3
"""redis with python as simple cache"""


import redis
from uuid import uuid4
from typing import Union, Optional, Callable


class Cache:
    """base class"""
    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float, None]) -> str:
        id = str(uuid4())
        self._redis.mset({id: data})
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
