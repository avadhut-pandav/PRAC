import random, math
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

random.seed(5)
items = [("Item"+str(i), random.randint(10,60), random.randint(10,50)) for i in range(6)]
CAPACITY = 80

def evaluate(decisions):
    value = sum(items[i][1] for i in range(len(decisions)) if decisions[i])
    weight = sum(items[i][2] for i in range(len(decisions)) if decisions[i])
    return (value, weight) if weight <= CAPACITY else (0, weight)

class Node:
    def __init__(self, decisions, parent=None):
        self.decisions = decisions
        self.parent = parent
        self.children = []
        self.visits = 0
        self.value = 0.0
        self.untried = [0,1] if len(decisions) < len(items) else []

def uct_select(node, c=1.4):
    return max(node.children, key=lambda n: n.value/n.visits + c*math.sqrt(math.log(node.visits)/n.visits))

def rollout(decisions):
    d = decisions[:]
    while len(d) < len(items):
        d.append(random.choice([0, 1]))
    value, weight = evaluate(d)
    return value

def mcts(iterations=800):
    root = Node([])
    for _ in range(iterations):
        node = root
        while not node.untried and node.children:
            node = uct_select(node)
        if node.untried:
            choice = node.untried.pop()
            child = Node(node.decisions + [choice], node)
            node.children.append(child)
            node = child
        reward = rollout(node.decisions)
        while node:
            node.visits += 1
            node.value += reward
            node = node.parent

    node, decisions = root, []
    while node.children:
        node = max(node.children, key=lambda n: n.visits)
        decisions.append(node.decisions[-1])
    while len(decisions) < len(items):
        decisions.append(0)
    return decisions

def draw_result(decisions):
    names = [items[i][0] for i in range(len(items))]
    values = [items[i][1] for i in range(len(items))]
    colors = ["#4CAF50" if d else "#CCCCCC" for d in decisions]
    plt.figure(figsize=(6,3))
    plt.bar(names, values, color=colors)
    plt.title("Knapsack via MCTS (green = selected)")
    plt.ylabel("Value")
    plt.xticks(rotation=45)
    plt.savefig("4b_knapsack_result.png", dpi=120, bbox_inches="tight")
    print("Saved visualization -> 4b_knapsack_result.png")

if __name__ == "__main__":
    decisions = mcts()
    value, weight = evaluate(decisions)
    print("Items:", items)
    print("Selected:", [items[i][0] for i in range(len(items)) if decisions[i]])
    print("Total value:", value, "| Total weight:", weight, "/", CAPACITY)
    draw_result(decisions)
