import random, math
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

random.seed(4)
DEPOT = (50, 50)
N_STOPS = 8
stops = [(random.uniform(0, 100), random.uniform(0, 100)) for _ in range(N_STOPS)]
locations = [DEPOT] + stops

