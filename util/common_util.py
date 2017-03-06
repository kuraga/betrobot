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
    if isinstance(object_or_list, list):
        return object_or_list
    else:
        return [ object_or_list ]
