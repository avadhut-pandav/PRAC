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

def hill_climbing():
    board = [random.randint(0, N - 1) for _ in range(N)]
    current = conflicts(board)
    while True:
        best_board, best_score = board, current
        for col in range(N):
            for row in range(N):
                if row == board[col]:
                    continue
                new_board = board[:]
                new_board[col] = row
                score = conflicts(new_board)
                if score < best_score:
                    best_board, best_score = new_board, score
        if best_score >= current:
            break
        board, current = best_board, best_score
    return board, current

