import unittest
import QLearning

class QLearningUnittest(unittest.TestCase):
    def test_1(self):
        qlearner = QLearning.QLearning([2,2], 2, 0.9)

        print("action 1")
        qlearner.ObserveAction([0,0], 1, [0,1], 1, learningRateScale = 1.0)
        print(qlearner.Q)
        print("visit")
        print(qlearner.visits)

        print("action 2")
        qlearner.ObserveAction([0,0], 1, [0,1], 1, learningRateScale = 1.0)
        print(qlearner.Q)
        print("visit")
        print(qlearner.visits)

ut = QLearningUnittest()
ut.test_1()