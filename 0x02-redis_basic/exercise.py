#!/usr/bin/env python3
"""
Writing Redis with python
"""
import redis
import uuid
from typing import Union, Callable

class Cache:
    """Cache class with redis"""

    def __init__(self, flush_on_init=False):
        self._redis = redis.Redis()
        if flush_on_init:
            self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

