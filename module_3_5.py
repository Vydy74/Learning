def get_multiplied_digits(number):
    str_number = str(number)

    # Возврат единичного числа
    if len(str_number) == 1:
        return int(str_number)

    # Извлекаем первую цифру числа
    first = int(str_number[0])

    # Вычисляем произведение оставшихся цифр и умножаем на первую цифру
    return first * get_multiplied_digits(int(str_number[1:]))


# Исходный код:
result = get_multiplied_digits(40203)
print(result)