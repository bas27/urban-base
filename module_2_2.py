further = 'Y'
while further.lower() != 'n':

    first = int(input('Введите первое значение: '))
    second = int(input('Введите второе значение: '))
    third = int(input('Введите третее значение: '))

    if first == second == third:
        print(3)
    elif first == second or first == third or second == third:
        print(2)
    else:
        print(0)

    further = input("Повторим? Y/N")