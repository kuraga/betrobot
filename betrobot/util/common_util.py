import os
import json


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


def count(function, iterable):
    n = 0
    for item in iterable:
        if function(item):
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
