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

def minimax(board, is_max):
    win = winner(board)
    if win == AI: return 1
    if win == HUMAN: return -1
    if EMPTY not in board: return 0

    scores = []
    for i in range(9):
        if board[i] == EMPTY:
            board[i] = AI if is_max else HUMAN
            scores.append(minimax(board, not is_max))
            board[i] = EMPTY
    return max(scores) if is_max else min(scores)

def best_move(board):
    best_score, move = -2, None
    for i in range(9):
        if board[i] == EMPTY:
            board[i] = AI
            score = minimax(board, False)
            board[i] = EMPTY
            if score > best_score:
                best_score, move = score, i
    return move

