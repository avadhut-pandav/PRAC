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

