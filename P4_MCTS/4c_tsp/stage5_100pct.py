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

class Node:
    def __init__(self, tour, parent=None):
        self.tour = tour
        self.parent = parent
        self.children = []
        self.visits = 0
        self.value = 0.0
        remaining = [c for c in range(N_CITIES) if c not in tour]
        self.untried = remaining

def uct_select(node, c=1.4):
    return max(node.children, key=lambda n: n.value/n.visits + c*math.sqrt(math.log(node.visits)/n.visits))

def rollout(tour):
    t = tour[:]
    remaining = [c for c in range(N_CITIES) if c not in t]
    random.shuffle(remaining)
    t += remaining
    return -tour_length(t)

def mcts(iterations=1000):
    root = Node([0])
    for _ in range(iterations):
        node = root
        while not node.untried and node.children:
            node = uct_select(node)
        if node.untried:
            nxt = node.untried.pop()
            child = Node(node.tour + [nxt], node)
            node.children.append(child)
            node = child
        reward = rollout(node.tour)
        while node:
            node.visits += 1
            node.value += reward
            node = node.parent
    node, tour = root, [0]
    while node.children:
        node = max(node.children, key=lambda n: n.visits)
        tour = node.tour
    while len(tour) < N_CITIES:
        remaining = [c for c in range(N_CITIES) if c not in tour]
        tour.append(remaining[0])
    return tour

def draw_route(tour):
    xs = [cities[i][0] for i in tour] + [cities[tour[0]][0]]
    ys = [cities[i][1] for i in tour] + [cities[tour[0]][1]]
    plt.figure(figsize=(5,5))
    plt.plot(xs, ys, "o-", color="purple")
    for idx, (x,y) in enumerate(cities):
        plt.text(x, y, str(idx), fontsize=9)
    plt.title(f"TSP route via MCTS (length={tour_length(tour):.1f})")
    plt.savefig("4c_tsp_result.png", dpi=120, bbox_inches="tight")
    print("Saved visualization -> 4c_tsp_result.png")

if __name__ == "__main__":
    tour = mcts()
    print("Tour:", tour)
    print("Tour length:", round(tour_length(tour), 2))
    draw_route(tour)
