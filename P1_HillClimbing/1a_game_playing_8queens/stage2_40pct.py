import random
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

N = 8

def conflicts(board):
    c = 0
    for i in range(N):
        for j in range(i + 1, N):
            if board[i] == board[j] or abs(board[i] - board[j]) == j - i:
                c += 1
    return c

