import random, math
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

random.seed(3)
durations = [4, 8, 3, 6, 2, 7]

def total_completion(order):
    t, total = 0, 0
    for job in order:
        t += durations[job]
        total += t
    return total

