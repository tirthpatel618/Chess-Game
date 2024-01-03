from ChessPiece import Piece
from ChessBoard import Board

class Horse(Piece):
     #inititalizing pieces and return
    def __init__(self, piece, colour, startx, starty, img):
        super().__init__(piece, colour, startx, starty, img)
    #method checking and giving all valid moves
    def valid_moves(self, board):
        x = self.startx
        y = self.starty
        moves = []
        #topside right
        if x < 6 and y > 0:
            if not board.has_piece(x + 2, y -1):
                moves.append([x +2, y-1])
            else:
                if board.which_piece(x+2, y-1).colour != self.colour:
                    moves.append([x+2, y-1])
                else:
                    pass
        #top right diagnol
        if x < 7 and y > 1:
            if not board.has_piece(x + 1, y -2):
                moves.append([x +1, y-2])
            else:
                if board.which_piece(x+1, y-2).colour != self.colour:
                    moves.append([x+1, y-2])
                else:
                    pass
        #Bottom side right
        if x < 6 and y < 7:
            if not board.has_piece(x + 2, y + 1):
                moves.append([x + 2, y+ 1])
            else:
                if board.which_piece(x+2, y+1).colour != self.colour:
                    moves.append([x+2, y+1])
                else:
                    pass
        #Bottom right diagnol
        if x < 7 and y < 6:
            if not board.has_piece(x + 1, y +2):
                moves.append([x +1, y+2])
            else:
                if board.which_piece(x+1, y+2).colour != self.colour:
                    moves.append([x+1, y+2])
                else:
                    pass
        #top side left
        if x > 1 and y > 0:
            if not board.has_piece(x -2 , y -1):
                moves.append([x -2, y-1])
            else:
                if board.which_piece(x-2, y-1).colour != self.colour:
                    moves.append([x-2, y-1])
                else:
                    pass
        #top left diagnol
        if x > 0 and y > 1:
            if not board.has_piece(x - 1, y -2):
                moves.append([x -1, y-2])
            else:
                if board.which_piece(x-1, y-2).colour != self.colour:
                    moves.append([x-1, y-2])
                else:
                    pass
        #Bottom side left
        if x > 1 and y < 7:
            if not board.has_piece(x - 2, y +1):
                moves.append([x -2, y+1])
            else:
                if board.which_piece(x-2, y+1).colour != self.colour:
                    moves.append([x-2, y+1])
                else:
                    pass
        #Bottom left diagnol
        if x > 0 and y < 6:
            if not board.has_piece(x - 1, y +2):
                moves.append([x -1, y+2])
            else:
                if board.which_piece(x-1, y+2).colour != self.colour:
                    moves.append([x-1, y+2])
                else:
                    pass
        return moves
