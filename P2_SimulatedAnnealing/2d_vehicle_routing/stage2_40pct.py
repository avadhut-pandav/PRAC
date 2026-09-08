import random, math
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

random.seed(4)
DEPOT = (50, 50)
N_STOPS = 8
stops = [(random.uniform(0, 100), random.uniform(0, 100)) for _ in range(N_STOPS)]
locations = [DEPOT] + stops

def dist(a, b):
    return math.hypot(a[0]-b[0], a[1]-b[1])

def route_length(order):
    full = [0] + order + [0]
    return sum(dist(locations[full[i]], locations[full[i+1]]) for i in range(len(full)-1))

