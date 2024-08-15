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
    def get(self, key: str, fn: Optional[Callable] = None) -> Union[None, str, int]:
        """
        Retrieves data from Redis, optionally applying a conversionn function.

        Args:
        key: The key to retrieve data for.
        fn: An optional callable that will be applied to the retrieved data
        """
        data = self._rdis.get(key)

        if data is None:
            return None

        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> Optional[str]:
        """
        Retrives data from Redis and converts it to a string using UTF-8
        """
        RETURN SELF.GET(KEY, FN=LAMBDA D: D.DECODE("UTF-8"))

    def get_int(self, key: str) -> Optional[int]:
        """
        Retrieves data from redis and converts it to an integer
        """
        try:
            return self.get(key, fn=int)
        except ValueError:
            return None

