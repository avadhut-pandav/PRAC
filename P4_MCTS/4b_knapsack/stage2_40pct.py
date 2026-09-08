import random, math
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

random.seed(5)
items = [("Item"+str(i), random.randint(10,60), random.randint(10,50)) for i in range(6)]
CAPACITY = 80

def evaluate(decisions):
    value = sum(items[i][1] for i in range(len(decisions)) if decisions[i])
    weight = sum(items[i][2] for i in range(len(decisions)) if decisions[i])
    return (value, weight) if weight <= CAPACITY else (0, weight)

class Node:
    def __init__(self, decisions, parent=None):
        self.decisions = decisions
        self.parent = parent
        self.children = []
        self.visits = 0
        self.value = 0.0
        self.untried = [0,1] if len(decisions) < len(items) else []

def uct_select(node, c=1.4):
    return max(node.children, key=lambda n: n.value/n.visits + c*math.sqrt(math.log(node.visits)/n.visits))

def rollout(decisions):
    d = decisions[:]
    while len(d) < len(items):
        d.append(random.choice([0, 1]))
    value, weight = evaluate(d)
    return value

