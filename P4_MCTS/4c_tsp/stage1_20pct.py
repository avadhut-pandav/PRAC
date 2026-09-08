import random, math
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

random.seed(6)
N_CITIES = 8
cities = [(random.uniform(0,100), random.uniform(0,100)) for _ in range(N_CITIES)]

def dist(a, b):
    return math.hypot(a[0]-b[0], a[1]-b[1])

def tour_length(tour):
    return sum(dist(cities[tour[i]], cities[tour[(i+1) % len(tour)]]) for i in range(len(tour)))

