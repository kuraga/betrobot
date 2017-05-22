def cartesian_product(list_, *others):
    if list_ is None:
        list_ = []

    result = []

    if len(others) == 0:
        new_item = list(list_)
        result.append(new_item)

    elif len(others) == 1:
        for item in others[0]:
            new_item = list(list_)
            new_item.append(item)
            result.append(new_item)

    else:
        for item in cartesian_product(list_, others[0]):
            result += cartesian_product(item, *others[1:])

    return result


def cartesian_product_of_dict_item(list_, key, *values):
    if list_ is None:
        list_ = [ {} ]

    result = []

    for item in list_:
        for value in values:
            new_item = dict(item)
            new_item[key] = value
            result.append(new_item)

    return result


def multiple_cartesian_product_of_dict_item(list_, dict_):
    result = list_
    for (key, values) in dict_.items():
        result = cartesian_product_of_dict_item(result, key, *values)

    return result


def make_sets_of_object_templates(args, kwargs, classes):
    return [ (class_, list(args), dict(kwargs)) for class_ in classes ]
