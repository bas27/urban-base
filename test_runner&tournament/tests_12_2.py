import unittest
import runner_and_tournament


class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usein = runner_and_tournament.Runner('Усэйн', 10)
        self.andrew = runner_and_tournament.Runner('Андрей', 9)
        self.nik = runner_and_tournament.Runner('Ник', 3)

    def test_tour_1(self):
        t1 = runner_and_tournament.Tournament(90, self.usein, self.nik)
        all_results = t1.start()
        last_key = max(all_results.keys())
        self.assertTrue(all_results[last_key] == 'Ник')
        self.all_results[self.id()] = all_results.values()
    def test_tour_2(self):
        t1 = runner_and_tournament.Tournament(90, self.andrew, self.nik)
        all_results = t1.start()
        last_key = max(all_results.keys())
        self.assertTrue(all_results[last_key] == 'Ник')

    def test_tour_3(self):
        t1 = runner_and_tournament.Tournament(90, self.usein, self.andrew, self.nik)
        all_results = t1.start()
        last_key = max(all_results.keys())
        self.assertTrue(all_results[last_key] == 'Ник')
        print(all_results)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results:
            print(result)


if __name__ == '__main__':
    unittest.main()
