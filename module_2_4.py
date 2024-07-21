# Исходный список
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]


primes = []
not_primes = []

# Проверка на простоту каждого числа из списка numbers
for number in numbers:

    is_prime = True

    # Проверка делителей числа
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break

    # Занесение числа в нужный список
    if is_prime and number != 1:
        primes.append(number)
    else:
        if number != 1:
            not_primes.append(number)

print(f"Список простых чисел: \n {primes}")
print(f"Список непростых чисел: \n {not_primes}")


