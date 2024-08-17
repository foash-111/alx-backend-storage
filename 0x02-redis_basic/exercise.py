#!/usr/bin/env python3
"""redis with python as simple cache"""


from redis import Redis
from uuid import uuid4
from typing import Union


class Cache:
    """base class"""
    def __init__(self) -> None:
        self._redis = Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        id = str(uuid4())
        self._redis.mset({str(id): data})
        return id
