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

def simulated_annealing(temp=1000, cooling=0.995, min_temp=1e-3):
    route = list(range(N_CITIES))
    random.shuffle(route)
    best, best_len = route[:], route_length(route)
    current_len = best_len
    while temp > min_temp:
        i, j = random.sample(range(N_CITIES), 2)
        new_route = route[:]
        new_route[i], new_route[j] = new_route[j], new_route[i]
        new_len = route_length(new_route)
        delta = new_len - current_len
        if delta < 0 or random.random() < math.exp(-delta / temp):
            route, current_len = new_route, new_len
            if new_len < best_len:
                best, best_len = new_route[:], new_len
        temp *= cooling
    return best, best_len

