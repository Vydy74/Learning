def print_params(a=1, b='строка', c=True):
    print(a, b, c)

# 1. Вызовы функции с разным количеством аргументов
print_params()

print_params(10)

print_params(10, 'другая строка')

print_params(10, 'другая строка', False)

print_params(b=25)
print_params(c=[1, 2, 3])


# 2. Распаковка параметров
values_list = [10, "Привет", False]
values_dict = {'a': 99, 'b': "Словарь", 'c': None}

print_params(*values_list)
print_params(**values_dict)



# Исходный код:
values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)