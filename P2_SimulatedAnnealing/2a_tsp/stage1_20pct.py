import random, math
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

random.seed(1)
N_CITIES = 10
cities = [(random.uniform(0, 100), random.uniform(0, 100)) for _ in range(N_CITIES)]

