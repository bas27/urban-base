import inspect
from pprint import pprint


def introspection_info(obj):

    dict_inspect = {'type': type(obj).__name__}
    dict_inspect['attributes'] = [attr for attr in dir(obj) if not attr.startswith('__')]

    return dict_inspect
#
# # help, dir, inspect, __name__, type, getattr, hasattr, callable, isinstance
#
# print(type((45)), dir(introspection_info(45)))


class Fighter:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def __str__(self):
        return f'name: {self.name}, health: {self.health}'


dark_knight = Fighter('Dark Knight', 100)
# print(dark_knight)



obj_info = introspection_info(dark_knight)

number = introspection_info(42)
print(obj_info)
print(number)