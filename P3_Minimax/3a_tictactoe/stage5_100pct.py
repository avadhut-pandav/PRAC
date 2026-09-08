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

def draw_board(board, filename):
    fig, ax = plt.subplots(figsize=(3, 3))
    for i in range(1, 3):
        ax.plot([i, i], [0, 3], color="black")
        ax.plot([0, 3], [i, i], color="black")
    for idx, mark in enumerate(board):
        r, c = divmod(idx, 3)
        if mark != EMPTY:
            ax.text(c + 0.5, 2.5 - r, mark, ha="center", va="center", fontsize=28)
    ax.set_xlim(0, 3); ax.set_ylim(0, 3)
    ax.set_xticks([]); ax.set_yticks([])
    plt.savefig(filename, dpi=120, bbox_inches="tight")

if __name__ == "__main__":
    board = [EMPTY] * 9

    human_moves = [0, 1, 2]
    turn = HUMAN
    move_no = 0
    while EMPTY in board and winner(board) is None:
        if turn == HUMAN:
            pos = human_moves[move_no] if move_no < len(human_moves) else\
                  next(i for i in range(9) if board[i] == EMPTY)
            board[pos] = HUMAN
        else:
            pos = best_move(board)
            board[pos] = AI
        print(f"Move {move_no+1}: {turn} -> position {pos}")
        turn = AI if turn == HUMAN else HUMAN
        move_no += 1

    result = winner(board) or "Draw"
    print("Result:", result)
    draw_board(board, "3a_tictactoe_result.png")
    print("Saved visualization -> 3a_tictactoe_result.png")
