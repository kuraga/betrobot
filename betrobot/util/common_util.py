import re
import datetime


def float_safe(x):
  try:
    return float(x)
  except (TypeError, ValueError):
    return None


def conjunct(*funcs):
    def conjunction(*args, **kwargs):
        for func in funcs:
            if not func(*args, **kwargs):
                return False
        return True

    conjunction.__name__ = 'conjunction-%s' % ('-'.join(func.__name__ for func in funcs),)

    return conjunction


def disjunct(*funcs):
    def disjunction(*args, **kwargs):
        for func in funcs:
            if func(*args, **kwargs):
                return True
            return False

    disjunction.__name__ = 'disjunction-%s' % ('-'.join(func.__name__ for func in funcs),)

    return disjunction


def recursive_sub(pattern, repl, string, *args, **kwargs):
    n = 1
    while n > 0:
        (string, n) = re.subn(pattern, repl, string, *args, **kwargs)
    return string


def eve_datetime(date_):
    return datetime.datetime.combine(date_, datetime.time(0, 0, 0, 0)) - datetime.timedelta(minutes=1)


def is_template(object_or_template):
    return (
        (isinstance(object_or_template, tuple) or isinstance(object_or_template, list)) and
        len(object_or_template) == 3 and
        isinstance(object_or_template[0], type) and
        (isinstance(object_or_template[1], tuple) or isinstance(object_or_template[1], list)) and
        isinstance(object_or_template[2], dict)
    )


def get_object(object_or_data):
    if not isinstance(object_or_data, tuple):
        return object_or_data
    else:
        (class_, args, kwargs) = object_or_data
        return class_(*args, **kwargs)
