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

def simulated_annealing(temp=500, cooling=0.99, min_temp=1e-3):
    solution = [random.randint(0, 1) for _ in items]
    best, best_val = solution[:], evaluate(solution)[0]
    current_val = best_val
    while temp > min_temp:
        i = random.randrange(len(items))
        new_solution = solution[:]
        new_solution[i] = 1 - new_solution[i]
        new_val, _ = evaluate(new_solution)
        delta = new_val - current_val
        if delta > 0 or random.random() < math.exp(delta / temp):
            solution, current_val = new_solution, new_val
            if new_val > best_val:
                best, best_val = new_solution[:], new_val
        temp *= cooling
    return best, best_val

