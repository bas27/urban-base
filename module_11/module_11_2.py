import inspect
from pprint import pprint


def introspection_info(obj):
    dict_inspect = {'type': type(obj).__name__}
    dict_inspect['attributes'] = [attr for attr in dir(obj) if not attr.startswith('__')]
    dict_inspect['methods'] = [method for method in dir(obj) if callable(getattr(obj, method))]
    try:
        dict_inspect['module'] = inspect.getmodule(obj).__name__
    except:
        dict_inspect['module'] = 'None'

    return dict_inspect


# # help, dir, inspect, __name__, type, getattr, hasattr, callable, isinstance


class Fighter:
    def __init__(self, name, health):
        self.name = name
        self.health = health
    def __str__(self):
        return f'name: {self.name}, health: {self.health}'


dark_knight = Fighter('Dark Knight', 100)
obj_info = introspection_info(dark_knight)

number = introspection_info(42)

pprint(obj_info)
pprint(number)
