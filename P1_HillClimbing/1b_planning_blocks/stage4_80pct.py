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

def draw_steps(steps):
    fig, axes = plt.subplots(1, len(steps), figsize=(2.2 * len(steps), 3))
    if len(steps) == 1:
        axes = [axes]
    for ax, state in zip(axes, steps):
        for pos, block in enumerate(state):
            color = "#4CAF50" if block == GOAL[pos] else "#F44336"
            ax.add_patch(plt.Rectangle((0, pos), 1, 0.9, color=color))
            ax.text(0.5, pos + 0.45, block, ha="center", va="center", fontsize=14, color="white")
        ax.set_xlim(0, 1); ax.set_ylim(0, len(state))
        ax.set_xticks([]); ax.set_yticks([])
    axes[0].set_title("Start")
    axes[-1].set_title("Goal reached")
    plt.savefig("1b_planning_result.png", dpi=120, bbox_inches="tight")
    print("Saved visualization -> 1b_planning_result.png")

