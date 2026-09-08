import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROWS, COLS = 6, 7
EMPTY, HUMAN, AI = 0, 1, 2

def create_board():
    return [[EMPTY] * COLS for _ in range(ROWS)]

def valid_moves(board):
    return [c for c in range(COLS) if board[0][c] == EMPTY]

def drop_piece(board, col, piece):
    for r in range(ROWS - 1, -1, -1):
        if board[r][col] == EMPTY:
            board[r][col] = piece
            return r

