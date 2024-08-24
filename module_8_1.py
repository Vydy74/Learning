def add_everything_up(a, b):
    try:
        result = a + b
        # Если результат - число, округляем до 3 знаков после запятой
        if isinstance(result, (int, float)):
            return f"{result:.3f}"
        return result
    except TypeError:
        # Если произошла ошибка типа, возвращаем строку из представлений a и b
        return str(a) + str(b)

# Примеры использования:
print(add_everything_up(123.456, 'строка'))  # Вывод: 123.456строка
print(add_everything_up('яблоко', 4215))     # Вывод: яблоко4215
print(add_everything_up(123.456, 7))         # Вывод: 130.456
print(add_everything_up('Привет', ' мир'))   # Вывод: Привет мир
print(add_everything_up(100, 200))           # Вывод: 300