immutable_var = (True, 1, 2, 8, 'Code', 1.4, [1, 2, 6, 45, 'cisco', 'mikrotik'])
print(immutable_var)
#immutable_var[0] = 'Punch' - кортеж не поддерживает переназначение объектов, которые в него входят, однако если сам объект поддерживает переназначение, например список в составе кортежа, тогда значения в списке возможно переназначить
immutable_var[-1][0] = 'cheese'
print(immutable_var)
print(immutable_var + tuple(['Гуси лебеди']))

mutable_list = [True, 1, 2, 8, 'Code', 1.4, [1, 2, 6, 45, 'cisco', 'mikrotik']]
print(mutable_list)
mutable_list[0] = 'Punch'
print(mutable_list)