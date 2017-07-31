import os
import plyvel
import pickle
import functools
import inspect
from betrobot.util.common_util import hashize


# TODO: Реализовать отключение кеша


_cache_path = os.path.join('data', 'cache.db')
_cache_db = plyvel.DB(_cache_path, create_if_missing=True, compression=None, lru_cache_size=256*1024*1024)


def _get_namespaced_db(namespace):
    if namespace is None:
        return _cache_db
    else:
        namespace_key = hashize(namespace) + b'__'
        return _cache_db.prefixed_db(namespace_key)


def cache_get(key, namespace=None):
    _cache = _get_namespaced_db(namespace)

    value = _cache.get(key)

    if value is not None:
        return pickle.loads(value)
    else:
        raise RuntimeError('value is unavailable in cache')


def cache_get_or_evaluate(key, func, *args, namespace=None, **kwargs):
    _cache = _get_namespaced_db(namespace)
    value = _cache.get(key)

    if value is not None:
        unpickled_value = pickle.loads(value)
    else:
        unpickled_value = func(*args, **kwargs)
        value = pickle.dumps(unpickled_value)
        _cache.put(key, value)

    return unpickled_value


def cache_put(key, unpickled_value, namespace=None):
    _cache = _get_namespaced_db(namespace)

    value = pickle.dumps(unpickled_value)
    _cache.put(key, value)


def cache_delete(key, namespace=None):
    _cache = _get_namespaced_db(namespace)

    _cache.delete(key)


def cache_clear(namespace=None):
    _cache = _get_namespaced_db(namespace)

    with _cache.iterator() as it:
        for k, v in it:
            _cache.delete(k)


# WARNING: Кешируемые функции, а также аргументы, являющиеся callable, должны иметь уникальный аттрибут __name__
def memoize(namespace_lambda=None):
    def decorator(func):

        @functools.wraps(func)
        def wrapped(*args, **kwargs):
            callargs = inspect.getcallargs(func, *args, **kwargs)
            key = hashize((func, callargs))
            namespace = namespace_lambda(*args, **kwargs) if namespace_lambda is not None else None
            return cache_get_or_evaluate(key, func, *args, namespace=namespace, **kwargs)

        return wrapped

    return decorator
