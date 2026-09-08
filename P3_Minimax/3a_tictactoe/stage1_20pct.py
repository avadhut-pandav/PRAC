import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

EMPTY, HUMAN, AI = " ", "X", "O"

def winner(b):
    lines = [b[0:3], b[3:6], b[6:9],
             b[0::3], b[1::3], b[2::3],
             [b[0], b[4], b[8]], [b[2], b[4], b[6]]]
    for line in lines:
        if line[0] != EMPTY and line[0] == line[1] == line[2]:
            return line[0]
    return None

