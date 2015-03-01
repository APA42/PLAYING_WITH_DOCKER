# -*- coding: utf-8 -*-

import redis
from redis_access import redis as redis_access


REDIS_SERVER_URI = "redis://192.168.50.100:6379"
KEY_PREFIX = "A_KEY_"
VALUE_PREFIX = "A_VALUE_"


def main():
    redis_connection = redis.StrictRedis.from_url(REDIS_SERVER_URI)
    my_redis_client = redis_access.RedisKeyValue(redis_connection)

    # Add elements
    for element in range(10):
        my_redis_client.set(KEY_PREFIX + str(element),
                            VALUE_PREFIX + str(element))

    print "Added 10 keys/values to redis"

    # Show elements
    for element in my_redis_client.keys(KEY_PREFIX + "*"):
        print "Key:{} Value:{}".format(element,my_redis_client.get(element))

if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print "FAILS:", exc
