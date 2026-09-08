import random
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

GOAL = ['A', 'B', 'C', 'D', 'E']

def score(state):

    return sum(1 for i in range(len(state)) if state[i] == GOAL[i])

