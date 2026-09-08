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

def check_winner(board, piece):
    for r in range(ROWS):
        for c in range(COLS - 3):
            if all(board[r][c+i] == piece for i in range(4)): return True
    for c in range(COLS):
        for r in range(ROWS - 3):
            if all(board[r+i][c] == piece for i in range(4)): return True
    for r in range(ROWS - 3):
        for c in range(COLS - 3):
            if all(board[r+i][c+i] == piece for i in range(4)): return True
            if all(board[r+3-i][c+i] == piece for i in range(4)): return True
    return False

def score_board(board, piece):
    return sum(row.count(piece) for row in board) - sum(row.count(3 - piece) for row in board)

