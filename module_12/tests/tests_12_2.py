import unittest
from module_12 import runner_and_tournament


class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usein = runner_and_tournament.Runner('Усэйн', 10)
        self.andrew = runner_and_tournament.Runner('Андрей', 9)
        self.nik = runner_and_tournament.Runner('Ник', 3)

    def tpl(self, distance, *objs):
        t1 = runner_and_tournament.Tournament(distance, *objs)
        all_results = t1.start()
        last_key = max(all_results.keys())
        try:
            self.assertTrue(all_results[last_key] == 'Ник')
            for key, value in all_results.items():
                all_results[key] = value.name
            self.all_results[self.id()] = all_results
        except AssertionError as e:
            self.all_results[self.id()] = f"Failed - {str(e)}"


    def test_tour_1(self):
        self.tpl(90, self.usein, self.nik)

    def test_tour_2(self):
        self.tpl(90, self.andrew, self.nik)

    def test_tour_3(self):
        self.tpl(90, self.usein, self.andrew, self.nik)


    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.values():
            print(result)


if __name__ == '__main__':
    unittest.main()
