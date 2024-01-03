
class Board:
    #initializing
    rect = (113, 113, 525, 525)
    startX = rect[0]
    startY = rect[1]
    #initializing the board and all variables
    def __init__(self):
        self.rows = 8
        self.cols = 8
        self.boardstate = []
    #method to make and reset the board
    def make_board(self):
        self.boardstate = [[0 for x in range(self.rows)]for y in range(self.cols)]
    #method to print the board in the style of a chess board
    def print_board(self):
        for x in range(self.rows):
            for y in range(self.cols):
                print(self.boardstate[y][x], end=" ")
            print()
    #method to check if tile entered is valid or not, used to check valid moves
    def isvalid_tile(self, x, y):
        if x > 0 and x < 7 and y > 0 and y < 7:
            return True
        else:
            False
    #method to set the piece on the actual board
    def set_piece(self, x, y, piece):
        self.boardstate[x][y] = piece
    #method checking if a tile on the board has a piece or not, used to check for valid moves
    def has_piece(self, x, y):
        if self.boardstate[x][y] == 0:
            return False
        else:
            return True
    #method that checks which piece is at a certain tile
    def which_piece(self, x, y):
        if self.has_piece(x, y):
            return self.boardstate[x][y]
        else:
            pass





