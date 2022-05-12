import numpy as np
import pickle
import random

class RL():
    def __init__(self, actions, epsilon = 0.06, learningRate = 0.5, discount = 0.9):
        self.Q = {}
        self.A = actions
        self.e = epsilon
        self.l = learningRate
        self.d = discount

    def setQ(self, Q):
        self.Q = Q

    def getQ(self, state, action):
        # default 0
        return self.Q.get((state, action), 0.0)

    def loadQ(self):
        #https://www.datacamp.com/community/tutorials/pickle-python-tutorial
        infile = open("LearnedData.txt", "rb") #read binary
        self.Q = pickle.load(infile)

    def saveQ(self):
        #https://www.datacamp.com/community/tutorials/pickle-python-tutorial
        f = open("LearnedData.txt", "wb") #write binary
        pickle.dump(self.Q, f)
        f.close()

    def getA(self, state):
        if random.random() < self.e:
            result = random.choice(self.A)
        else:
            TxtList = [self.getQ(state, a) for a in self.A]
            max_q = max(TxtList)
            index = np.where(np.array(TxtList) == max_q)
            result = self.A[random.choice(index[0])]
        return result

class QLearing(RL):
    def updateQ(self, state, action, new_state, reward):
        q = self.Q.get((state, action), None)
        if q is None:
            self.Q[(state, action)] = reward
        else:
            newMax = max([self.getQ(new_state, a) for a in self.A])
            self.Q[(state, action)] = q + self.l * (reward + self.d * newMax - q)

