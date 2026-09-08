import random, math
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

random.seed(1)
N_CITIES = 10
cities = [(random.uniform(0, 100), random.uniform(0, 100)) for _ in range(N_CITIES)]

def dist(a, b):
    return math.hypot(a[0]-b[0], a[1]-b[1])

def route_length(route):
    return sum(dist(cities[route[i]], cities[route[(i+1) % len(route)]]) for i in range(len(route)))

