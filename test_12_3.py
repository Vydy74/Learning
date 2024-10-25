import unittest
from runner_and_tournament import Runner, Tournament
import random


class TournamentTest(unittest.TestCase):
    is_frozen = True
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usain = Runner("Усэйн", 10)
        self.andrey = Runner("Андрей", 9)
        self.nick = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for key in [1, 2, 3]:
            if key in cls.all_results:
                result = cls.all_results[key]
                formatted_result = {place: runner.name for place, runner in result.items()}
                print(formatted_result)
    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_usain_and_nick(self):
        tournament = Tournament(90, self.usain, self.nick)
        result = tournament.start()
        self.all_results[1] = result  # Используем индекс 1 для первого теста
        last_place = max(result.keys())
        self.assertTrue(result[last_place] == "Ник")

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_andrey_and_nick(self):
        tournament = Tournament(90, self.andrey, self.nick)
        result = tournament.start()
        self.all_results[2] = result  # Используем индекс 2 для второго теста
        last_place = max(result.keys())
        self.assertTrue(result[last_place] == "Ник")

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_usain_andrey_and_nick(self):
        tournament = Tournament(90, self.andrey, self.usain, self.nick)
        result = tournament.start()
        self.all_results[3] = result  # Используем индекс 3 для третьего теста
        last_place = max(result.keys())
        self.assertTrue(result[last_place] == "Ник")

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        # Создаем объект класса Runner с произвольным именем
        bigun1 = Runner("Vasya")

        # Вызываем метод walk 10 раз
        for _ in range(10):
            bigun1.walk()
        print(f"{bigun1} високий гори шёль {bigun1.distance} km")
        self.assertEqual(bigun1.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        bigun2 = Runner("Manya")

        for _ in range(10):
            bigun2.run()
        print(f"{bigun2} прямой дорога бижаль {bigun2.distance} km")
        self.assertEqual(bigun2.distance, 100)

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


if __name__ == '__main__':
    unittest.main()