import os
import plyvel
import pickle
import functools
import inspect
import hashlib


# TODO: Реализовать удаление элемента из кеша, очистку кеша
# TODO: Реализовать отключение кеша


_cache_path = os.path.join('data', 'cache.db')
_cache_db = plyvel.DB(_cache_path, create_if_missing=True, compression=None, lru_cache_size=256*1024*1024)


def cache_get(key):
    value = _cache_db.get(key)

    if value is not None:
        return pickle.loads(value)
    else:
        raise RuntimeError('value is unavailable in cache')


def cache_get_or_evaluate(key, func, *args, **kwargs):
    value = _cache_db.get(key)

    if value is not None:
        unpickled_value = pickle.loads(value)
    else:
        unpickled_value = func(*args, **kwargs)
        value = pickle.dumps(unpickled_value)
        _cache_db.put(key, value)

    return unpickled_value


def cache_put(key, unpickled_value):
    value = pickle.dumps(unpickled_value)
    _cache_db.put(key, value)


def hashize(obj, hasher=None):
    if hasher is None:
        hasher = hashlib.sha512()  # TODO: Выбрать алгоритм по-быстрее

    hasher.update(obj.__class__.__name__.encode('ascii'))

    # FIXME: Как определять функции?
    if hasattr(obj, '__code__'):
        hashize(obj.__name__, hasher=hasher)
    elif type(obj) in (list, tuple):
        for v in obj:
            hashize(v, hasher=hasher)
    elif type(obj) == dict:
        for k in obj:
            hashize(k, hasher=hasher)
            hashize(obj[k], hasher=hasher)
    else:
        to_hash = pickle.dumps(obj)
        hasher.update(to_hash)

    return hasher.hexdigest().encode('ascii')


def memoize(func):
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        callargs = inspect.getcallargs(func, *args, **kwargs)
        key = hashize((func, callargs))

        return cache_get_or_evaluate(key, func, *args, **kwargs)

    return wrapped
