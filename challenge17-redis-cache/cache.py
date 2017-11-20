import redis
import json
from functools import wraps


class RedisCache:
    def __init__(self, redis_client):
        self._redis = redis_client

    def cache(self, timeout=0):
        def deco(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
#                skwargs = sorted(kwargs.items())
                key = func.__name__
                print('function name of func %s' % func.__name__)
                print('key: %s' %key)
                if self._redis.exists(key):
                    data = self._redis.get(key)
                    print('from cache')
                    return json.loads(data.decode())
                else:
                    data = func(*args, **kwargs)
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



if __name__ == '__main__':
    print('function name of execute %s ' % execute.__name__)
    print(execute('10', a = 1, b = 2, c = 3))



