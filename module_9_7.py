def is_prime(func):
    def wrapper(*args, **kwargs):
        value = func(*args, **kwargs)
        print(value)
        for i in range(2, value-1):
            if value % i == 0:
                return 'Составное'
        return 'Простое'
    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c


result = sum_three(3, 3, 6)
print(result)
