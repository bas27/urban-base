#Работа со словарями

my_dict = {'Nik': 2001, 'Alex': 1984, 'Li': 1995}
print(my_dict)
print(my_dict['Alex'])
print(my_dict.get('Bob'))
my_dict.update({'Zorge': 1992, 
                'Ivan': 2010})
print(my_dict)
ext = my_dict.pop('Alex')
print(ext)
print(my_dict)

#Работа с множествами

my_set = set([1, 2, 3, 8, 1, 3, (True, 1, 4.5)])
print(my_set)
my_set.update([15, 18])
print(my_set)
my_set.remove((True, 1, 4.5))
print(my_set)
