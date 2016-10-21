import sys
sys.path.append('./')
sys.path.append('./util')


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
    if type(object_or_list) is list:
        return object_or_list
    else:
        return [ object_or_list ]


def safe_get(dict_or_value, key):
    if type(dict_or_value) is dict:
        return dict_or_value[key]
    else:
        return dict_or_value

