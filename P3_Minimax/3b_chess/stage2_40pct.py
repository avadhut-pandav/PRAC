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

