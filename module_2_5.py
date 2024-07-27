def get_matrix(rows, bars, value):

    # Проверка на корректность размеров
    if rows <= 0 or rows <= 0:
        return []

    # Создание пустого списка
    matrix = []

    # Первый цикл для создания строк матрицы
    for _ in range(rows):
        row = []
        matrix.append(row)

        # Второй  цикл для заполнения столбцов матрицы
        for _ in range(bars):
            row.append(value)

    return matrix

# Тестирование функции
result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)