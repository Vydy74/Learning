import unittest
from runner_and_tournament import Runner, Tournament

class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usain = Runner("Усэйн", 10)
        self.andrey = Runner("Андрей", 9)
        self.nick = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for key in [1, 2, 3]:  # Задаем порядок вывода(Намучался я с этим)
            if key in cls.all_results:
                result = cls.all_results[key]
                formatted_result = {place: runner.name for place, runner in result.items()}
                print(formatted_result)

    def test_usain_and_nick(self):
        tournament = Tournament(90, self.usain, self.nick)
        result = tournament.start()
        self.all_results[1] = result  # Используем индекс 1 для первого теста
        last_place = max(result.keys())
        self.assertTrue(result[last_place] == "Ник")

    def test_andrey_and_nick(self):
        tournament = Tournament(90, self.andrey, self.nick)
        result = tournament.start()
        self.all_results[2] = result  # Используем индекс 2 для второго теста
        last_place = max(result.keys())
        self.assertTrue(result[last_place] == "Ник")
    """
Ошибка в классе Runner заключается в умножении скорости на два, из за этого бегуны
с небольшой разницей скорости проходят расстояние за одинаковое колличество итераций
"""
    def test_usain_andrey_and_nick(self):
        tournament = Tournament(90, self.andrey, self.usain, self.nick)
        result = tournament.start()
        self.all_results[3] = result  # Используем индекс 3 для третьего теста
        last_place = max(result.keys())
        self.assertTrue(result[last_place] == "Ник")


if __name__ == '__main__':
    unittest.main()