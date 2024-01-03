from ChessPiece import Piece
from ChessKing import King
from ChessBoard import Board

class Rook(Piece):
    #inititalizing pieces and return
    def __init__(self, piece, colour, startx, starty, img):
        super().__init__(piece, colour, startx, starty, img)
    #method checking and giving all valid moves
    def valid_moves(self, board):
        x = self.startx
        y = self.starty
        moves = []

        #Up
        for i in range(y-1, -1, -1):
            if not board.has_piece(x, i):
                moves.append([x, i])
            else:
                if board.which_piece(x, i).colour != self.colour:
                    moves.append([x, i])
                    break
                else:
                    break
                    
        #Down
        for i in range(y+1, 8):
            if not board.has_piece(x, i):
                moves.append([x, i])
            else:
                if board.which_piece(x, i).colour != self.colour:
                    moves.append([x, i])
                    break
                else:
                    break
        #Right
        for i in range(x+1, 8):
            if not board.has_piece(i, y):
                moves.append([i, y])
            else:
                if board.which_piece(i, y).colour != self.colour:
                    moves.append([i, y])
                    break
                else:
                    break
        #left
        for i in range(x-1, -1, -1):
            if not board.has_piece(i, y):
                moves.append([i, y])
            else:
                if board.which_piece(i, y).colour != self.colour:
                    moves.append([i, y])
                    break
                else:
                    break
        #castling
        if self.first:
            if x == 0 and y == 7:
                if board.which_piece(1, 7) == King:
                    moves.append([2, 7])
            elif x == 7 and y == 7:
                if board.which_piece(5, 7) == King:
                    moves.append([4, 7])
            elif x == 0 and y == 0:
                if board.which_piece(2, 0) == King:
                    moves.append([3, 0])
            elif x == 7 and y == 0:
                if board.which_piece(6, 0) == King:

                    moves.append([5, 0])
            else:
                pass
        else:
            pass
        return moves
