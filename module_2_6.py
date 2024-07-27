def generate_password(n):
    result = []
    for i in range(1, 21):
        for j in range(i+1, 21):
            if i + j == n or (i + j != 0 and n % (i + j) == 0):
                result.append(str(i) + str(j))
    return ''.join(result)


n = int(input("Введите число от 3 до 20: "))
if 3 <= n <= 20:
    password = generate_password(n)
    print(f"Пароль для числа {n}: {password}")
else:
    print("Число должно быть от 3 до 20")