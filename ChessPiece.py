from ChessBoard import Board

class Piece:
    #initializing the variables in the piece
    def __init__(self, piece, colour, startx, starty, img):
        self.piece = piece
        self.colour = colour
        self.startx = startx
        self.starty = starty
        self.img = img
        self.first = True

    #initiliazing what the piece returns
    def __str__(self):
        name = self.colour[0]+self.piece
        return name
    #method to find all valid moves for a piece
    def valid_moves(self, board):
        x = self.startx
        y = self.starty
        moves = []
        return moves
    #method to move pieces in the board
    def move_piece(self, endx, endy, board):
        move = [endx, endy]
        if move in self.valid_moves(board):
            board.boardstate[endx][endy] = self
            board.boardstate[self.startx][self.starty] = 0
            self.startx = endx
            self.starty = endy
            self.first = False


