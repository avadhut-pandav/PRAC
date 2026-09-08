import random
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

GOAL = ['A', 'B', 'C', 'D', 'E']

def score(state):

    return sum(1 for i in range(len(state)) if state[i] == GOAL[i])

def hill_climbing(state):
    current = score(state)
    steps = [state[:]]
    while current < len(GOAL):
        best_state, best_score = state, current
        for i in range(len(state)):
            for j in range(i + 1, len(state)):
                new_state = state[:]
                new_state[i], new_state[j] = new_state[j], new_state[i]
                s = score(new_state)
                if s > best_score:
                    best_state, best_score = new_state, s
        if best_score <= current:
            break
        state, current = best_state, best_score
        steps.append(state[:])
    return state, steps

