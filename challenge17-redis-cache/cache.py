import redis
import json


r = redis.StrictRedis(host='127.0.0.1', db=0)


class RedisCache:
    def __init__(self, redis_client):
        self._redis = redis_client

    def cache(self, timeout=0):
        def deco(func):
            def wrapper(*args, **kwargs):
                key = (args, kwargs)
                if self._redis.exists(key):
                    data = self._redis.get(key)
                    return json.loads(data.decode())

                else:
                    data = func(*args, **kwargs)
                    data_json = json.dumps(data)
                    self._redis.set(key, data_json)
                    self._redis.expire(key, timeout)

                    return data
            return wrapper

        return deco






cache = RedisCache(r)
@cache.cache(timeout=10)
def execute(n):
    
    return {'n': n, 'n2': n * 2}


if __name__ == '__main__':
    print(execute('10'))



