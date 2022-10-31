#!/usr/bin/env python3
"""
reddis
"""
import redis


class Cache:
    def __init__(self):
        """ constructor - store an instance of the Redis client as a private
        variable named _redis and flush the instance using flushdb """
        self._redis = redis.Redis()
        self._redis.flushdb()
