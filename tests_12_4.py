import unittest
from rt_with_exceptions import Runner
import logging




class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        # Создаем объект класса Runner с произвольным именем

        try:
            bigun1 = Runner("Vasya", -5)
            logging.info("'test_walk' - выполнен успешно")
            # Вызываем метод walk 10 раз
            for _ in range(10):
                bigun1.walk()
            print(f"{bigun1} високий гори шёль {bigun1.distance} km")
            self.assertEqual(bigun1.distance, 50)
        except:
            logging.warning("Неверная скорость для Runner", exc_info=True)
            print("Ошибка: Введите корректное значение скорости")

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        try:
            bigun2 = Runner(334)
            logging.info("'test_run' - выполнен успешно")

            for _ in range(10):
                bigun2.run()
            print(f"{bigun2} прямой дорога бижаль {bigun2.distance} km")
            self.assertEqual(bigun2.distance, 100)
        except:
            logging.warning("Неверный тип данных для объекта Runner")
            print("Ошибка: Введите корректные данные для имени")

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
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

    logging.basicConfig(level=logging.INFO, filemode="w", filename="runner_tests.log", encoding="utf-8",
                        format="%(asctime)s, | %(levelname)s, | %(message)s")
if __name__ == '__main__':

    unittest.main()
