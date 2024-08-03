def calculate_structure_sum(data): # Функция с аргументом
    total = 0
    if isinstance(data, (list, tuple, set)): # списки, кортежи, множества
        for item in data:
            total += calculate_structure_sum(item)
    elif isinstance(data, dict): # Словари
        for key, value in data.items():
            total += calculate_structure_sum(key)
            total += calculate_structure_sum(value)
    elif isinstance(data, int): # Целые числа
        total += data
    elif isinstance(data, str): # Строки
        total += len(data)

    return total

data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
