from ChessPiece import Piece
from ChessBoard import Board

class King(Piece):
    #inititalizing pieces and return
    def __init__(self, piece, colour, startx, starty, img):
        super().__init__(piece, colour, startx, starty, img)
    #method checking and giving all valid moves
    def valid_moves(self, board):
        x = self.startx
        y = self.starty
        moves = []

        try:
            #top right diagnol
            if y > 0 and x < 7:
                if not board.has_piece(x+1, y-1):
                    moves.append([x+1, y-1])
                if board.has_piece(x+1, y-1):
                    if board.which_piece(x+1, y-1).colour != self.colour:
                        moves.append([x+1, y-1])
            #right
            if x < 7:
                if not board.has_piece(x+1, y):
                    moves.append([x+1, y])
                if board.has_piece(x+1, y):
                    if board.which_piece(x+1, y).colour != self.colour:
                        moves.append([x+1, y])
            #bottom right diagnol
            if y < 7 and x < 7:
                if not board.has_piece(x+1, y+1):
                    moves.append([x+1, y+1])
                if board.has_piece(x+1, y+1):
                    if board.which_piece(x+1, y+1).colour != self.colour:
                        moves.append([x+1, y+1])
            #up
            if y > 0:
                if not board.has_piece(x, y-1):
                    moves.append([x, y-1])
                if board.has_piece(x, y-1):
                    if board.which_piece(x, y-1).colour != self.colour:
                        moves.append([x, y-1])
            #down
            if y < 7:
                if not board.has_piece(x, y+1):
                    moves.append([x, y+1])
                if board.has_piece(x, y+1):
                    if board.which_piece(x, y+1).colour != self.colour:
                        moves.append([x, y+1])
            #top left
            if x > 0 and y > 0:
                if not board.has_piece(x-1, y-1):
                    moves.append([x-1, y-1])
                if board.has_piece(x-1, y-1):
                    if board.which_piece(x-1, y-1).colour != self.colour:
                        moves.append([x-1, y-1])
            #bottom left
            if x > 0 and y < 7:
                if not board.has_piece(x-1, y+1):
                    moves.append([x-1, y+1])
                if board.has_piece(x-1, y+1):
                    if board.which_piece(x-1, y+1).colour != self.colour:
                        moves.append([x-1, y+1])
            #left
            if x > 0:
                if not board.has_piece(x-1, y):
                    moves.append([x-1, y])
                if board.has_piece(x-1, y):
                    if board.which_piece(x-1, y).colour != self.colour:
                        moves.append([x-1, y])
            #castling
            if self.first:
                if self.colour == "White":
                    #shortside white
                    if board.which_piece(0, 7).first:
                        if not board.has_piece(1, 7) and not board.has_piece(2, 7):
                            wleftcastle = True
                            moves.append([1, 7])
                    #longside white
                    if board.which_piece(7, 7).first:
                        if not board.has_piece(4, 7) and not board.has_piece(5, 7) and not board.has_piece(6, 7):
                            wrightcastle = True
                            moves.append([5, 7])
                else:
                    #shortside black
                    if board.which_piece(7, 0).first:
                        if not board.has_piece(6, 0) and not board.has_piece(5, 0):
                            brightcastle = True
                            moves.append([6, 0])
                    #longside black
                    if board.which_piece(0, 0):
                        if not board.has_piece(1, 0) and not board.has_piece(2, 0) and not board.has_piece(3, 0):
                            bleftcastle = True
                            moves.append([2, 0])
            else:
                pass
        except:
            pass
        return moves
    def move_piece(self, endx, endy, board):
        move = [endx, endy]
        #extra moves to castle
        if move == [1, 7]:
            board.which_piece(0, 7).move_piece(2, 7, board)
            board.boardstate[endx][endy] = self
            board.boardstate[self.startx][self.starty] = 0
            self.startx = endx
            self.starty = endy
            self.first = False
        elif move == [5, 7]:
            board.which_piece(7, 7).move_piece(4, 7, board)
            board.boardstate[endx][endy] = self
            board.boardstate[self.startx][self.starty] = 0
            self.startx = endx
            self.starty = endy
            self.first = False
        elif move == [2, 0]:
            board.which_piece(0, 0).move_piece(3, 0, board)
            board.boardstate[endx][endy] = self
            board.boardstate[self.startx][self.starty] = 0
            self.startx = endx
            self.starty = endy
            self.first = False
        elif move == [6, 0]:
            board.which_piece(7, 0).move_piece(5, 0, board)
            board.boardstate[endx][endy] = self
            board.boardstate[self.startx][self.starty] = 0
            self.startx = endx
            self.starty = endy
            self.first = False
        else:
            if move in self.valid_moves(board):
                board.boardstate[endx][endy] = self
                board.boardstate[self.startx][self.starty] = 0
                self.startx = endx
                self.starty = endy
                self.first = False
