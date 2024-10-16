def is_prime(func):
    def wrapper(*args, **kwargs):
        value = func(*args, **kwargs)
        if value == 1:
            print('Составное')
        else:
            prime_flag = False
            for i in range(2, int(value**0.5) + 1):
                if value % i == 0:
                    prime_flag = True
                    break
            if prime_flag:
                print('Составное')
            else:
                print('Простое')
        return value
    return wrapper


@is_prime
def sum_three(a, b, c):
    # print(a + b + c)
    return a + b + c


result = sum_three(11, 0, 0)
print(result)
