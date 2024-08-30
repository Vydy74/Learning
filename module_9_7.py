def sum_three(a, b, c):

    return a + b + c


def is_prime(func):

    def wrapper(a, b, c):
        result = func(a, b, c)
        if result > 1:
            for i in range(3, int(result ** 0.5) + 1, 2):
                if result % i == 0:
                    print("Составное число")
                    break
            else:
                print("Простое число")

        else:
            print("Составное число")
        return result
    return wrapper

sum_three = is_prime(sum_three)

result = sum_three(2, 3, 6)
print(result)
