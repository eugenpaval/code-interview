import unittest
from src.runningUpSteps import run

class RunningUpStepsTestSuite(unittest.TestCase):
    def test1(self):
        x = run(10)
        print(x)
        self.assertEqual(x, 274)