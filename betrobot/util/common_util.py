import os
import json
import functools
import datetime


def float_safe(x):
  try:
    return float(x)
  except (TypeError, ValueError):
    return None


def input_multiline(*args):
  while True:
    try:
      line = input()
      yield line
    except EOFError:
      return


def count(function, iterable, *args, **kwargs):
    n = 0
    for item in iterable:
        if function(item, *args, **kwargs):
            n += 1
            
    return n


def get_first(function, iterable):
    for item in iterable:
        if function(item):
            return item

    return None


def list_wrap(object_or_list):
    if isinstance(object_or_list, list):
        return object_or_list
    else:
        return [ object_or_list ]


def safe_get(dict_or_value, key, default=None):
    if isinstance(dict_or_value, dict):
        return dict_or_value.get(key, default)
    else:
        return dict_or_value


def safe_read_json(file_path, default):
    if os.path.exists(file_path):
        with open(file_path, 'rt', encoding='utf-8') as f:
            return json.load(f)
    else:
        return default


def conjunction(*funcs):
    def conjunct(*args, **kwargs):
        return functools.reduce(lambda total_result, next_function: total_result and next_function(*args, **kwargs), funcs, True)

    return conjunct


def disjunction(*funcs):
    def disjunct(*args, **kwargs):
        return functools.reduce(lambda total_result, next_function: total_result or next_function(*args, **kwargs), funcs, False)

    return disjunct


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
