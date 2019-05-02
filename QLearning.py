import math
import collections
import operator
import random
import numpy as np


class QLearning(object):

    def __init__(self, stateSpaceShape, numActions, discountRate):
        self.stateSpaceShape = stateSpaceShape
        self.numActions = numActions
        self.discountRate = discountRate

        #initialize q table
        self.Q = dict()
        self.visits = dict()

        #for item in stateSpaceShape:
        #    for i in range(item):

        

    def GetAction(self, currentState, learningMode, randomActionRate=-1, actionProbabilityBase=1.8):
        currentState = self.build_state(currentState)

        if currentState not in self.Q:
            self.Q[currentState] = dict()
            for action in range(self.numActions):
                self.Q[currentState][action] = 0.0

        if learningMode:
            if random.random() <= randomActionRate:
                return random.randint(0, self.numActions - 1)
            else:
                probList = dict()
                #denominator = 0.0
                #for action in range(self.numActions):
                #    denominator += math.pow(actionProbabilityBase, self.Q[currentState][action])
                for action in range(self.numActions):
                    numerator = math.pow(actionProbabilityBase, self.Q[currentState][action])
                    probList[action] = numerator
                    #probList[action] = numerator / denominator

                return self.weighted_random_choice(probList)

        else:
            maxQ = self.get_maxQ(currentState)
            actions = []
            for key, value in self.Q[currentState].items():
                if value == maxQ:
                    actions.append(key)
            if len(actions) != 0:
                action = random.choice(actions)
            return action

    def ObserveAction(self, oldState, action, newState, reward, learningRateScale):
        oldState = self.build_state(oldState)
        newState = self.build_state(newState)

        if oldState not in self.visits:
            self.visits[oldState] = dict()
            for currAct in range(self.numActions):
                self.visits[oldState][currAct] = 0.0
        
        self.visits[oldState][action] += 1

        alpha = 1.0 / (1.0 + (learningRateScale * self.visits[oldState][action]))
        self.Q[oldState][action] = ((1 - alpha) * self.Q[oldState][action]) + alpha * (reward + (self.discountRate * self.get_maxQ(newState)))

    def get_maxQ(self, state):
        if state not in self.Q:
            self.Q[state] = dict()
            for action in range(self.numActions):
                self.Q[state][action] = 0.0
        maxQ = max(self.Q[state].values())
        return maxQ
        
    def build_state(self, features):
        #return int("".join(map(lambda feature: str(int(feature)), features)))
        return ",".join(map(lambda feature: str(int(feature)), features))

    def weighted_random_choice(self, choices):
        max = sum(choices.values())
        pick = random.uniform(0, max)
        current = 0
        for key, value in choices.items():
            current += value
            if current > pick:
                return key
        return 0