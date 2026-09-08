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

def simulated_annealing(temp=1000, cooling=0.995, min_temp=1e-3):
    order = list(range(1, N_STOPS + 1))
    random.shuffle(order)
    best, best_len = order[:], route_length(order)
    current_len = best_len
    while temp > min_temp:
        i, j = random.sample(range(len(order)), 2)
        new_order = order[:]
        new_order[i], new_order[j] = new_order[j], new_order[i]
        new_len = route_length(new_order)
        delta = new_len - current_len
        if delta < 0 or random.random() < math.exp(-delta / temp):
            order, current_len = new_order, new_len
            if new_len < best_len:
                best, best_len = new_order[:], new_len
        temp *= cooling
    return best, best_len

def draw_route(order):
    full = [0] + order + [0]
    xs = [locations[i][0] for i in full]
    ys = [locations[i][1] for i in full]
    plt.figure(figsize=(5, 5))
    plt.plot(xs, ys, "o-", color="tab:green")
    plt.plot(DEPOT[0], DEPOT[1], "s", color="red", markersize=12, label="Depot")
    for idx, (x, y) in enumerate(stops, start=1):
        plt.text(x, y, str(idx), fontsize=9)
    plt.legend()
    plt.title(f"Vehicle Route via Simulated Annealing (length={route_length(order):.1f})")
    plt.savefig("2d_vrp_result.png", dpi=120, bbox_inches="tight")
    print("Saved visualization -> 2d_vrp_result.png")

