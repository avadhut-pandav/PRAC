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

def draw_board(board):
    fig, ax = plt.subplots(figsize=(5, 5))
    for r in range(N):
        for c in range(N):
            color = "#EEEED2" if (r + c) % 2 == 0 else "#769656"
            ax.add_patch(plt.Rectangle((c, r), 1, 1, color=color))
    for col, row in enumerate(board):
        ax.text(col + 0.5, row + 0.5, "Q", ha="center", va="center", fontsize=20, color="red")
    ax.set_xlim(0, N); ax.set_ylim(0, N)
    ax.set_xticks([]); ax.set_yticks([])
    ax.set_title(f"8-Queens via Hill Climbing (conflicts={conflicts(board)})")
    plt.savefig("1a_8queens_result.png", dpi=120, bbox_inches="tight")
    print("Saved visualization -> 1a_8queens_result.png")

if __name__ == "__main__":
    solution = None
    for attempt in range(1, 200):
        board, score = hill_climbing()
        if score == 0:
            solution = board
            print(f"Solved in {attempt} restart(s): {board}")
            break
    if solution is None:
        solution, _ = hill_climbing()
        print("Best found (not perfect):", solution)
    draw_board(solution)
