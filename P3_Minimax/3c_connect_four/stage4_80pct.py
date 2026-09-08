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

def minimax(board, depth, is_max):
    if check_winner(board, AI): return 100, None
    if check_winner(board, HUMAN): return -100, None
    moves = valid_moves(board)
    if depth == 0 or not moves:
        return score_board(board, AI), None

    best_col = moves[0]
    if is_max:
        best_score = -float("inf")
        for col in moves:
            b2 = [row[:] for row in board]
            drop_piece(b2, col, AI)
            score, _ = minimax(b2, depth - 1, False)
            if score > best_score:
                best_score, best_col = score, col
    else:
        best_score = float("inf")
        for col in moves:
            b2 = [row[:] for row in board]
            drop_piece(b2, col, HUMAN)
            score, _ = minimax(b2, depth - 1, True)
            if score < best_score:
                best_score, best_col = score, col
    return best_score, best_col

def draw_board(board, filename):
    fig, ax = plt.subplots(figsize=(6, 5))
    colors = {EMPTY: "white", HUMAN: "red", AI: "yellow"}
    for r in range(ROWS):
        for c in range(COLS):
            circle = plt.Circle((c, ROWS - r - 1), 0.4, color=colors[board[r][c]], ec="black")
            ax.add_patch(circle)
    ax.set_facecolor("blue")
    ax.set_xlim(-0.5, COLS - 0.5); ax.set_ylim(-0.5, ROWS - 0.5)
    ax.set_xticks([]); ax.set_yticks([])
    ax.set_title("Connect Four via Minimax")
    plt.savefig(filename, dpi=120, bbox_inches="tight", facecolor="lightblue")

