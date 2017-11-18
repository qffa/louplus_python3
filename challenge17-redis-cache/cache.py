import redis
import json


class RedisCache:
    def __init__(self, redis_client):
        self._redis = redis_client

    def cache(self, timeout=0):
        def deco(func):
            def wrapper(*args, **kwargs):
                skwargs = sorted(kwargs.items())
                key = (args, skwargs)
                if self._redis.exists(key):
                    data = self._redis.get(key)
                    print('from cache')
                    return json.loads(data.decode())
                else:
                    data = func(*args, **kwargs)
                    assert isinstance(data, dict), "%s doesn't return dictiionary" %func
                    jdata = json.dumps(data)
                    self._redis.set(key, jdata)
                    self._redis.expire(key, timeout)

                    return data
            return wrapper

        return deco



r = redis.StrictRedis(host='127.0.0.1', db=0)
cache = RedisCache(r)

@cache.cache(timeout=10)
def execute(n, a, b, c):
    
    return {'n': n, 'n2': n * 2}
#    return 0


if __name__ == '__main__':
    print(execute('10', a = 1, b = 2, c = 3))



