import unittest
import tests_12_1
import tests_12_2
import tests_12_3

# import test_runner_tournament

testST = unittest.TestSuite()
testST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_1.RunnerTest))
testST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_2.TournamentTest))
testST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
testST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))



start = unittest.TextTestRunner(verbosity=2)
start.run(testST)