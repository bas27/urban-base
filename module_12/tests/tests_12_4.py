import unittest
from module_12 import rt_with_exceptions as rt
import logging

logging.basicConfig(level=logging.INFO, filemode="w", encoding="utf-8", filename="runner_tests.log",
                    format='%(asctime)s | %(levelname)s | %(message)s')
class RunnerTest(unittest.TestCase):
    is_frozen = False
    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_walk(self):
        """
        Test walk method
        """
        try:
            r1 = rt.Runner('Alex', speed=-5)
            for _ in range(10):
                r1.walk()
            self.assertEqual(r1.distance, 50)
            logging.info(f'"test_walk" выполнен успешно')
        except Exception as e:
            logging.warning(f"Неверная скорость для Runner\n{e}")

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_run(self):
        """
        Test run method
        """
        try:
            r1 = rt.Runner(Alex)
            for _ in range(10):
                r1.run()
            self.assertEqual(r1.distance, 100)
            logging.info(f'"test_run" выполнен успешно')
        except Exception as e:
            logging.warning(f"Неверный тип данных для объекта Runner\n{e}")

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_challenge(self):
        r1 = rt.Runner('Alex')
        r2 = rt.Runner('Den')
        for _ in range(10):
            r1.walk()
            r2.run()
        self.assertNotEqual(r1.distance, r2.distance)

class TournamentTest(unittest.TestCase):
    is_frozen = False
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usein = rt.Runner('Усэйн', 10)
        self.andrew = rt.Runner('Андрей', 9)
        self.nik = rt.Runner('Ник', 3)

    def tpl(self, distance, *objs):
        t1 = rt.Tournament(distance, *objs)
        all_results = t1.start()
        last_key = max(all_results.keys())
        try:
            self.assertTrue(all_results[last_key] == 'Ник')
            for key, value in all_results.items():
                all_results[key] = value.name
            self.all_results[self.id()] = all_results
        except AssertionError as e:
            self.all_results[self.id()] = f"Failed - {str(e)}"

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_tour_1(self):
        self.tpl(90, self.usein, self.nik)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_tour_2(self):
        self.tpl(90, self.andrew, self.nik)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_tour_3(self):
        self.tpl(90, self.usein, self.andrew, self.nik)


    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.values():
            print(result)


if __name__ == '__main__':
    unittest.main()