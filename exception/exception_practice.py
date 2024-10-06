def calc(line):
    operand1, operator, operand2 = line.split()
    operand1, operand2 = int(operand1), int(operand2)
    # print(operand1, operator, operand2)

'''    if operator == '+':
        print(f'Результат: {operand1 + operand2}')
    if operator == '-':
            print(f'Результат: {operand1 - operand2}')
    if operator == '//':
            print(f'Результат: {operand1 // operand2}')
    if operator == '*':
            print(f'Результат: {operand1 * operand2}')
    if operator == '/':
            print(f'Результат: {operand1 / operand2}')
    if operator == '%':
            print(f'Результат: {operand1 % operand2}')'''

count = 0

with open('calc.txt') as f:
    for line in f:
        count += 1
        try:
            calc(line)

        except Exception as e:
            if 'unpack' in e.args[0]:
                print(f'Ошибка  в строке {count}, не хватает данных для расчета')
            else:
                print(f'Ошибка в строке {count}, нельзя перевести в число')