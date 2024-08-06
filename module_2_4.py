numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

primes = []
not_primes = []

for i in numbers:
    is_prime = True
    if i == 1:
        continue
    for j in range(1, i):
        if i % j == 0 and j != 1 and i != j:
            is_prime = False
            not_primes.append(i)
            break
    if is_prime:
        primes.append(i)
print(primes)
print(not_primes)

#Время выполнения кода можно отслеживать так:

# import time
#
# start_time = time.time()
# # Ваш код здесь
# end_time = time.time()
#
# execution_time = end_time - start_time
# print(f"Время выполнения: {execution_time} секунд")