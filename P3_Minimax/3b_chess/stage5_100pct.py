import chess
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

PIECE_VALUE = {chess.PAWN: 1, chess.KNIGHT: 3, chess.BISHOP: 3,
               chess.ROOK: 5, chess.QUEEN: 9, chess.KING: 0}

def evaluate(board):
    score = 0
    for piece_type, value in PIECE_VALUE.items():
        score += value * len(board.pieces(piece_type, chess.WHITE))
        score -= value * len(board.pieces(piece_type, chess.BLACK))
    return score

def minimax(board, depth, is_max):
    if depth == 0 or board.is_game_over():
        return evaluate(board), None

    best_move = None
    if is_max:
        best_score = -float("inf")
        for move in board.legal_moves:
            board.push(move)
            score, _ = minimax(board, depth - 1, False)
            board.pop()
            if score > best_score:
                best_score, best_move = score, move
    else:
        best_score = float("inf")
        for move in board.legal_moves:
            board.push(move)
            score, _ = minimax(board, depth - 1, True)
            board.pop()
            if score < best_score:
                best_score, best_move = score, move
    return best_score, best_move

UNICODE = {'P':'P','N':'N','B':'B','R':'R','Q':'Q','K':'K',
           'p':'p','n':'n','b':'b','r':'r','q':'q','k':'k'}

def draw_board(board, filename):
    fig, ax = plt.subplots(figsize=(5, 5))
    for r in range(8):
        for c in range(8):
            color = "#EEEED2" if (r + c) % 2 == 0 else "#769656"
            ax.add_patch(plt.Rectangle((c, r), 1, 1, color=color))
    for square, piece in board.piece_map().items():
        c, r = chess.square_file(square), chess.square_rank(square)
        symbol = piece.symbol()
        color = "white" if symbol.isupper() else "black"
        ax.text(c + 0.5, r + 0.5, UNICODE[symbol], ha="center", va="center",
                fontsize=16, color=color,
                bbox=dict(boxstyle="circle", facecolor="gray" if color=="black" else "lightgray"))
    ax.set_xlim(0, 8); ax.set_ylim(0, 8)
    ax.set_xticks([]); ax.set_yticks([])
    ax.set_title("Chess position after Minimax move")
    plt.savefig(filename, dpi=120, bbox_inches="tight")

if __name__ == "__main__":
    board = chess.Board()
    print(board, "\n")
    DEPTH = 2
    for i in range(4):
        maximizing = board.turn == chess.WHITE
        score, move = minimax(board, DEPTH, maximizing)
        if move is None:
            break
        board.push(move)
        print(f"Ply {i+1}: {'White' if maximizing else 'Black'} plays {move} (eval={score})")
    print("\nFinal position:\n", board)
    draw_board(board, "3b_chess_result.png")
    print("Saved visualization -> 3b_chess_result.png")
