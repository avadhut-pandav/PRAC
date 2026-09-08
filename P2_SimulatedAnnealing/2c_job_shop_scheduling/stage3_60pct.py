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

def simulated_annealing(temp=1000, cooling=0.98, min_temp=1e-3):
    order = list(range(len(durations)))
    random.shuffle(order)
    best, best_cost = order[:], total_completion(order)
    current_cost = best_cost
    while temp > min_temp:
        i, j = random.sample(range(len(order)), 2)
        new_order = order[:]
        new_order[i], new_order[j] = new_order[j], new_order[i]
        new_cost = total_completion(new_order)
        delta = new_cost - current_cost
        if delta < 0 or random.random() < math.exp(-delta / temp):
            order, current_cost = new_order, new_cost
            if new_cost < best_cost:
                best, best_cost = new_order[:], new_cost
        temp *= cooling
    return best, best_cost

