from flask_caching import Cache

cache = Cache()

def getCache(key,callback):
    data = cache.get(key)
    if data:
        return data
    data = callback()
    cache.set(key,data)
    return data
