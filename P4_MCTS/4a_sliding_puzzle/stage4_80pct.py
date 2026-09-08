import random, math, copy
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

GOAL = (1,2,3,4,5,6,7,8,0)
SIZE = 3

def get_moves(state):
    idx = state.index(0)
    r, c = divmod(idx, SIZE)
    moves = []
    for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
        nr, nc = r+dr, c+dc
        if 0 <= nr < SIZE and 0 <= nc < SIZE:
            n_idx = nr*SIZE+nc
            new_state = list(state)
            new_state[idx], new_state[n_idx] = new_state[n_idx], new_state[idx]
            moves.append(tuple(new_state))
    return moves

def heuristic(state):
    return sum(1 for i in range(9) if state[i] != GOAL[i])

class Node:
    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent
        self.children = []
        self.visits = 0
        self.value = 0.0
        self.untried = get_moves(state)

def uct_select(node, c=1.4):
    return max(node.children, key=lambda n: n.value/n.visits + c*math.sqrt(math.log(node.visits)/n.visits))

def rollout(state, depth=10):
    for _ in range(depth):
        if state == GOAL:
            return 1.0
        state = random.choice(get_moves(state))
    return 1.0 / (1 + heuristic(state))

def mcts(root_state, iterations=500):
    root = Node(root_state)
    for _ in range(iterations):
        node = root

        while not node.untried and node.children:
            node = uct_select(node)

        if node.untried:
            move = node.untried.pop()
            child = Node(move, node)
            node.children.append(child)
            node = child

        reward = rollout(node.state)

        while node:
            node.visits += 1
            node.value += reward
            node = node.parent
    return max(root.children, key=lambda n: n.visits).state

def draw_state(state, filename, title):
    fig, ax = plt.subplots(figsize=(3, 3))
    for i, val in enumerate(state):
        r, c = divmod(i, SIZE)
        color = "white" if val == 0 else "#4CAF50"
        ax.add_patch(plt.Rectangle((c, SIZE-r-1), 1, 1, facecolor=color, edgecolor="black"))
        if val != 0:
            ax.text(c+0.5, SIZE-r-1+0.5, str(val), ha="center", va="center", fontsize=18)
    ax.set_xlim(0, SIZE); ax.set_ylim(0, SIZE)
    ax.set_xticks([]); ax.set_yticks([])
    ax.set_title(title)
    plt.savefig(filename, dpi=120, bbox_inches="tight")

