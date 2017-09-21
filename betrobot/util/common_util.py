import re
import datetime
import pickle
import binascii
import uuid
import warnings


def float_safe(x):
  try:
    return float(x)
  except (TypeError, ValueError):
    return None


def count(what, where):
    c = 0

    for item in where:
        if item == what:
            c += 1

    return c


def find_index(what, where):
    for i in range(len(where)):
        if what == where[i]:
            return i

    return None


def wrap(obj):
    if obj is None:
        return []
    elif isinstance(obj, list) or isinstance(obj, tuple):
        return obj
    else:
        return [ obj ]


def truth(*args, **kwargs):
    return True


def falsehood(*args, **kwargs):
    return False


def conjunct(*funcs):
    def conjunction(*args, **kwargs):
        for func in funcs:
            if not func(*args, **kwargs):
                return False
        return True

    conjunction.__name__ = 'conjunction__%s' % ('__'.join(func.__name__ for func in funcs),)

    return conjunction


def disjunct(*funcs):
    def disjunction(*args, **kwargs):
        for func in funcs:
            if func(*args, **kwargs):
                return True
            return False

    disjunction.__name__ = 'disjunction__%s' % ('__'.join(func.__name__ for func in funcs),)

    return disjunction


def recursive_sub(pattern, repl, string, *args, **kwargs):
    n = 1
    while n > 0:
        (string, n) = re.subn(pattern, repl, string, *args, **kwargs)
    return string


def eve_datetime(date_):
    return datetime.datetime.combine(date_, datetime.time(0, 0, 0, 0)) - datetime.timedelta(minutes=1)


def get_identifier():
    return str(uuid.uuid4())


def is_template(object_or_template):
    return (
        (isinstance(object_or_template, tuple) or isinstance(object_or_template, list)) and
        len(object_or_template) == 3 and
        isinstance(object_or_template[0], type) and
        (isinstance(object_or_template[1], tuple) or isinstance(object_or_template[1], list)) and
        isinstance(object_or_template[2], dict)
    )


def get_object(object_or_template):
    if not is_template(object_or_template):
        return object_or_template
    else:
        (class_, args, kwargs) = object_or_template
        return class_(*args, **kwargs)


def _hashize_piece(obj, representation):
    size = len(representation)

    hash_bytes = obj.__class__.__name__.encode('utf-8')
    hash_bytes += ('(%x)<' % (size,)).encode('utf-8')
    hash_bytes += representation
    hash_bytes += '>'.encode('utf-8')

    hash_ = binascii.crc32(hash_bytes) & 0xffffffff
    hash_bytes = hash_.to_bytes(4, 'little', signed=False)

    return hash_bytes


def hashize(obj):
    if hasattr(obj, '__code__'):
        if hasattr(obj, '__name__'):
            representation = hashize(obj.__name__)
        else:
            warnings.warn('hashing of a callable without __name__ attribute')
            representation = hashize(obj.__code__.co_code)
    elif type(obj) in (list, tuple):
        representation = bytes()
        for v in obj:
            representation += hashize(v)
    elif type(obj) == dict:
        representation = bytes()
        for k in sorted(obj.keys()):
            representation += hashize(k)
            representation += hashize(obj[k])
    else:
        representation = pickle.dumps(obj)

    hash_bytes = _hashize_piece(obj, representation)

    return hash_bytes


def is_value_valid(data, by, value):
    return value in data[by].values


def get_value(data, by, value, which, default=None):
    if not is_value_valid(data, by, value):
        return default

    # WARNING: Возвращаем первое значение, удовлетворяющее условию
    return data.loc[data[by] == value, which].values[0]
