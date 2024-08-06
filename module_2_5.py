def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for _ in range(m):
            matrix[i].append(value)
    return matrix


result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)

'''
Вывод на консоль (так должно получиться):
[[10, 10], [10, 10]]
[[42, 42, 42, 42, 42], [42, 42, 42, 42, 42], [42, 42, 42, 42, 42]]
[[13, 13], [13, 13], [13, 13], [13, 13]]
'''
