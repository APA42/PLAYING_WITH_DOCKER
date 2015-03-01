# -*- coding: utf-8 -*-


class RedisKeyValue(object):
    def __init__(self, redis_client):
        self.redis_client = redis_client

    def set(self, key, value):
        self.redis_client.set(key, value)

    def get(self, key):
        return self.redis_client.get(key)

    def keys(self, pattern):
        return self.redis_client.keys(pattern)

    def exists(self, key):
        return self.redis_client.exists(key)

    def delete(self, key):
        self.redis_client.delete(key)
