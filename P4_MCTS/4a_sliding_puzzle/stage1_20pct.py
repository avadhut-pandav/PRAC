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

