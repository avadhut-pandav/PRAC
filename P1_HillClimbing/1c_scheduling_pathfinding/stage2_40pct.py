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

