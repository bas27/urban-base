'''
Весь подсчёт должен выполняться одним вызовом функции.
Рекомендуется применить рекурсивный вызов функции, для каждой внутренней структуры.
Т.к. каждая структура может содержать в себе ещё несколько элементов, можно использовать параметр *args
Для определения типа данного используйте функцию isinstance.
'''


def calculate_structure_sum(*args):
    total = 0
    for element in args:
        if isinstance(element, dict):
            for key, value in element.items():
                total += calculate_structure_sum(value) + calculate_structure_sum(key)
        elif isinstance(element, (list, tuple, set)):
            total += calculate_structure_sum(*element)
        elif isinstance(element, str):
            total += len(element)
        elif isinstance(element, int):
            total += element

    return total


# data_structure = [1,2, [1, 2, 3], 'hello',{'a': 4, 'b': 5}]
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]
# result 99

result = calculate_structure_sum(data_structure)
print(result)
