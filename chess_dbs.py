import chess
import sys
import random

class SimpleEngine:
    def __init__(self):
        self.board = chess.Board()

    def evaluate(self, board):
        if board.is_checkmate():
            if board.turn:
                return -9999
            else:
                return 9999
        if board.is_stalemate():
            return 0
        if board.is_insufficient_material():
            return 0

        wp = len(board.pieces(chess.PAWN, chess.WHITE))
        bp = len(board.pieces(chess.PAWN, chess.BLACK))
        wn = len(board.pieces(chess.KNIGHT, chess.WHITE))
        bn = len(board.pieces(chess.KNIGHT, chess.BLACK))
        wb = len(board.pieces(chess.BISHOP, chess.WHITE))
        bb = len(board.pieces(chess.BISHOP, chess.BLACK))
        wr = len(board.pieces(chess.ROOK, chess.WHITE))
        br = len(board.pieces(chess.ROOK, chess.BLACK))
        wq = len(board.pieces(chess.QUEEN, chess.WHITE))
        bq = len(board.pieces(chess.QUEEN, chess.BLACK))

        material = 100*(wp-bp)+320*(wn-bn)+330*(wb-bb)+500*(wr-br)+900*(wq-bq)

        # Add a small random factor to the evaluation to promote more diverse moves
        return material + 0.01 * random.random()

    def alphabeta(self, alpha, beta, depthleft):
        bestscore = -9999
        if depthleft == 0:
            return self.evaluate(self.board)
        for move in self.board.legal_moves:
            self.board.push(move)
            score = -self.alphabeta(-beta, -alpha, depthleft-1)
            self.board.pop()
            if score >= beta:
                return score
            if score > bestscore:
                bestscore = score
            if score > alpha:
                alpha = score
        return bestscore

    def search(self, depth):
        bestMove = chess.Move.null()
        bestValue = -99999
        alpha = -100000
        beta = 100000
        for move in self.board.legal_moves:
            self.board.push(move)
            boardValue = -self.alphabeta(-beta, -alpha, depth)
            self.board.pop()
            if boardValue > bestValue:
                bestValue = boardValue
                bestMove = move
        return bestMove

    def play(self):
        depth = 1
        best_move = self.search(depth)
        while depth < 2: # Let's cap at depth 4 for performance reasons
            depth += 1
            try_move = self.search(depth)
            if self.board.is_capture(try_move):
                best_move = try_move
                break
            best_move = try_move
        self.board.push(best_move)
        return best_move

engine = SimpleEngine()

while True:
    msg = sys.stdin.readline().strip()
    if msg == 'isready':
        print('readyok')
    elif msg.startswith('position'):
        moves = msg.split(' ')[1:]
        if moves[0] == 'startpos':
            engine.board.set_fen(chess.STARTING_FEN)
            moves = moves[2:] # get moves from 'moves e2e4 ...'
        elif moves[0] == 'fen':
            engine.board.set_fen(' '.join(moves[1:7]))
            moves = moves[8:] # get moves from 'moves e2e4 ...'
        # apply moves if any
        for move in moves:
            engine.board.push_san(move)
    elif msg.startswith('go'):
        best_move = engine.play()
        print(f'bestmove {best_move}')
    sys.stdout.flush()
