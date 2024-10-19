import unittest
from runner import Runner

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        # Создаем объект класса Runner с произвольным именем
        bigun1 = Runner("Vasya")

        # Вызываем метод walk 10 раз
        for _ in range(10):
            bigun1.walk()
        print(f"{bigun1} високий гори шёль {bigun1.distance} km")
        self.assertEqual(bigun1.distance, 50)

    def test_run(self):
        bigun2 = Runner("Manya")

        for _ in range(10):
            bigun2.run()
        print(f"{bigun2} прямой дорога бижаль {bigun2.distance} km")
        self.assertEqual(bigun2.distance, 100)

    def test_chalenge(self):
        bigun1 = Runner("Bubba")
        bigun2 = Runner("Puppa")
        for _ in range(10):
            bigun1.run()
            bigun2.walk()
        print(f"{bigun1} пробегит {bigun1.distance} km")
        print(f"{bigun2} пишьком шоль {bigun2.distance} km")
        if True:
            self.assertNotEqual(bigun1.distance, bigun2.distance, "Дистанции должны быть разными")
            print(f"{bigun1} болшой {bigun2} савсэм малэнкий, карочи нэадинаковий")



if __name__ == "__main__":
    unittest.main()

