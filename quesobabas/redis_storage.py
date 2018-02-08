import logging

logging.basicConfig(level=logging.INFO)

import os
import redis

def init_redis():
    host = os.environ["REDIS_HOST"]
    port = os.environ["REDIS_PORT"]

    conn_pool = redis.ConnectionPool(host=host, port=port, db=0)

    return redis.Redis(connection_pool=conn_pool)

connection = init_redis()
