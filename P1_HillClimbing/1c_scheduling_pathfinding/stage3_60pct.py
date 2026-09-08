import random
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

def total_waiting_time(order, durations):
    t, wait = 0, 0
    for job in order:
        wait += t
        t += durations[job]
    return wait

def hill_climb_schedule(durations):
    order = list(range(len(durations)))
    random.shuffle(order)
    current = total_waiting_time(order, durations)
    improved = True
    while improved:
        improved = False
        for i in range(len(order)):
            for j in range(i + 1, len(order)):
                new_order = order[:]
                new_order[i], new_order[j] = new_order[j], new_order[i]
                w = total_waiting_time(new_order, durations)
                if w < current:
                    order, current, improved = new_order, w, True
    return order, current

def draw_gantt(order, durations):
    fig, ax = plt.subplots(figsize=(6, 2))
    t = 0
    for job in order:
        ax.barh(0, durations[job], left=t, color="skyblue", edgecolor="black")
        ax.text(t + durations[job] / 2, 0, f"J{job}", ha="center", va="center")
        t += durations[job]
    ax.set_yticks([]); ax.set_xlabel("Time")
    ax.set_title("Job Schedule (Hill Climbing)")
    plt.savefig("1c_scheduling_result.png", dpi=120, bbox_inches="tight")
    print("Saved visualization -> 1c_scheduling_result.png")

def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def hill_climb_path(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    pos, path = start, [start]
    while pos != goal:
        neighbours = [(pos[0]+dr, pos[1]+dc) for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]]
        neighbours = [n for n in neighbours if 0 <= n[0] < rows and 0 <= n[1] < cols and grid[n[0]][n[1]] == 0]
        if not neighbours:
            break
        best = min(neighbours, key=lambda n: manhattan(n, goal))
        if manhattan(best, goal) >= manhattan(pos, goal):
            break
        pos = best
        path.append(pos)
    return path

