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

def draw_grid(grid, path, start, goal):
    fig, ax = plt.subplots(figsize=(5, 5))
    rows, cols = len(grid), len(grid[0])
    for r in range(rows):
        for c in range(cols):
            color = "black" if grid[r][c] == 1 else "white"
            ax.add_patch(plt.Rectangle((c, rows - r - 1), 1, 1, facecolor=color, edgecolor="gray"))
    for (r, c) in path:
        ax.add_patch(plt.Rectangle((c, rows - r - 1), 1, 1, facecolor="yellow", edgecolor="gray"))
    sr, sc = start; gr, gc = goal
    ax.text(sc + 0.5, rows - sr - 1 + 0.5, "S", ha="center", va="center", fontsize=14)
    ax.text(gc + 0.5, rows - gr - 1 + 0.5, "G", ha="center", va="center", fontsize=14)
    ax.set_xlim(0, cols); ax.set_ylim(0, rows)
    ax.set_xticks([]); ax.set_yticks([])
    ax.set_title("Path Finding via Hill Climbing")
    plt.savefig("1c_pathfinding_result.png", dpi=120, bbox_inches="tight")
    print("Saved visualization -> 1c_pathfinding_result.png")

