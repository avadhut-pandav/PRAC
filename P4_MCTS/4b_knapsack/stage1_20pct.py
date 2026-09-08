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

