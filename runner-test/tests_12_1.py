import unittest
import runner


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        """
        Test walk method
        """
        r1 = runner.Runner('Alex')
        for _ in range(10):
            r1.walk()
        self.assertEqual(r1.distance, 50)

    def test_run(self):
        """
        Test run method
        """

        r1 = runner.Runner('Alex')
        for _ in range(10):
            r1.run()
        self.assertEqual(r1.distance, 100)

    def test_challenge(self):
        r1 = runner.Runner('Alex')
        r2= runner.Runner('Den')
        for _ in range(10):
            r1.walk()
            r2.run()
        self.assertNotEqual(r1.distance, r2.distance)


if __name__ == '__main__':
    unittest.main()