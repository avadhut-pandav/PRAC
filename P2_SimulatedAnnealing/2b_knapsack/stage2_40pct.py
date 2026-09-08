import random, math
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

random.seed(2)
items = [("Item"+str(i), random.randint(10,60), random.randint(10,50)) for i in range(8)]
CAPACITY = 100

def evaluate(solution):
    value = sum(items[i][1] for i in range(len(items)) if solution[i])
    weight = sum(items[i][2] for i in range(len(items)) if solution[i])
    if weight > CAPACITY:
        value = 0
    return value, weight

