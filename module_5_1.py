class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        # Проверка номера этажа
        if 1 <= new_floor <= self.number_of_floors:
            # Вывод номеров этажей от 1 до new_floor
            for floor in range(1, new_floor + 1):
                print(floor)
        else:
            # Вывод сообщения об ошибке
            print("Такого этажа не существует")

# Проверка
h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)

h1.go_to(5)
h2.go_to(10)
