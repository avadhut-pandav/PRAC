import random, math
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

random.seed(2)
items = [("Item"+str(i), random.randint(10,60), random.randint(10,50)) for i in range(8)]
CAPACITY = 100

