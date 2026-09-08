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

