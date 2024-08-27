first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

# Генератор для first_result
first_result = (len(f) - len(s) for f, s in zip(first, second) if len(f) != len(s))

# Генератор для second_result
second_result = (len(first[i]) == len(second[i]) for i in range(len(first)))

# Выводим результаты
print(list(first_result))
print(list(second_result))