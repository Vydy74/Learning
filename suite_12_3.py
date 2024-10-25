import unittest
import test_12_3 as TT


Test_S = unittest.TestSuite()
Test_S.addTest(unittest.TestLoader().loadTestsFromTestCase(TT.TournamentTest))
Test_S.addTest(unittest.TestLoader().loadTestsFromTestCase(TT.RunnerTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(Test_S)


