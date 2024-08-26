#1 создание функции
def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params(b=25)
print_params(c=[1, 2, 3])

#2 Распаковка параметров
values_list = [789, 4.6, 333]
values_dict = {'a':'Hello', 'b': True, 'c': 123}

print_params(*values_list)
print_params(**values_dict)

#3.Распаковка + отдельные параметры
values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)

