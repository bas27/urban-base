import unittest
from module_12 import runner_


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        """
        Test walk method
        """
        r1 = runner_.Runner('Alex')
        for _ in range(10):
            r1.walk()
        self.assertEqual(r1.distance, 50)

    def test_run(self):
        """
        Test run method
        """

        r1 = runner_.Runner('Alex')
        for _ in range(10):
            r1.run()
        self.assertEqual(r1.distance, 100)

    def test_challenge(self):
        r1 = runner_.Runner('Alex')
        r2 = runner_.Runner('Den')
        for _ in range(10):
            r1.walk()
            r2.run()
        self.assertNotEqual(r1.distance, r2.distance)


if __name__ == '__main__':
    unittest.main()