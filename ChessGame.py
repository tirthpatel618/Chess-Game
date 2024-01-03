from ChessBoard import Board
from ChessPawn import Pawn
from ChessBishop import Bishop
from ChessQueen import Queen
from ChessRook import Rook
from ChessHorse import Horse
from ChessKing import King
#making the pieces and the board
board1 = Board()
board1.make_board()
#white pawns
wpawn1 = Pawn("Pawn1", "White", 0, 6, 'white_pawn.png')
wpawn2 = Pawn("Pawn2", "White", 1, 6, "")
wpawn3 = Pawn("Pawn3", "White", 2, 6, "")
wpawn4 = Pawn("Pawn4", "White", 3, 6, "")
wpawn5 = Pawn("Pawn5", "White", 4, 6, "")
wpawn6 = Pawn("Pawn6", "White", 5, 6, "")
wpawn7 = Pawn("Pawn7", "White", 6, 6, "")
wpawn8 = Pawn("Pawn8", "White", 7, 6, "")
#black pawns
bpawn1 = Pawn("Pawn1", "Black", 0, 1, "")
bpawn2 = Pawn("Pawn2", "Black", 1, 1, "")
bpawn3 = Pawn("Pawn3", "Black", 2, 1, "")
bpawn4 = Pawn("Pawn4", "Black", 3, 1, "")
bpawn5 = Pawn("Pawn5", "Black", 4, 1, "")
bpawn6 = Pawn("Pawn6", "Black", 5, 1, "")
bpawn7 = Pawn("Pawn7", "Black", 6, 1, "")
bpawn8 = Pawn("Pawn8", "Black", 7, 1, "")
#white pieces
wrook1 = Rook("Rook1", "White", 0, 7, "")
wrook2 = Rook("Rook2", "White", 7, 7, "")
whorse1 = Horse("Horse1", "White", 1, 7, "")
whorse2 = Horse("Horse2", "White", 6, 7, "")
wbishop1 = Bishop("Bishop1", "White", 2, 7, "")
wbishop2 = Bishop("Bishop2", "White", 5, 7, "")
wqueen = Queen("Queen", "White", 4, 7, "")
wking = King("King", "White", 3, 7, "")
#black pieces
brook1 = Rook("Rook1", "Black", 0, 0, "")
brook2 = Rook("Rook2", "Black", 7, 0, "")
bhorse1 = Horse("Horse1", "Black", 1, 0, "")
bhorse2 = Horse("Horse2", "Black", 6, 0, "")
bbishop1 = Bishop("Bishop1", "Black", 2, 0, "")
bbishop2 = Bishop("Bishop2", "Black", 5, 0, "")
bqueen = Queen("Queen", "Black", 3, 0, "")
bking = King("King", "Black", 4, 0, "")
#class for the game
class Game:
    def __init__(self, board):
        self.board = board
    #method to set all pieces on the board
    def set_game(self):

        self.board.set_piece(0, 6, wpawn1)
        self.board.set_piece(1, 6, wpawn2)
        self.board.set_piece(2, 6, wpawn3)
        self.board.set_piece(3, 6, wpawn4)
        self.board.set_piece(4, 6, wpawn5)
        self.board.set_piece(5, 6, wpawn6)
        self.board.set_piece(6, 6, wpawn7)
        self.board.set_piece(7, 6, wpawn8)

        self.board.set_piece(0, 1, bpawn1)
        self.board.set_piece(1, 1, bpawn2)
        self.board.set_piece(2, 1, bpawn3)
        self.board.set_piece(3, 1, bpawn4)
        self.board.set_piece(4, 1, bpawn5)
        self.board.set_piece(5, 1, bpawn6)
        self.board.set_piece(6, 1, bpawn7)
        self.board.set_piece(7, 1, bpawn8)

        self.board.set_piece(0, 7, wrook1)
        self.board.set_piece(7, 7, wrook2)
        self.board.set_piece(1, 7, whorse1)
        self.board.set_piece(6, 7, whorse2)
        self.board.set_piece(2, 7, wbishop1)
        self.board.set_piece(5, 7, wbishop2)
        self.board.set_piece(4, 7, wqueen)
        self.board.set_piece(3, 7, wking)

        self.board.set_piece(0, 0, brook1)
        self.board.set_piece(7, 0, brook2)
        self.board.set_piece(1, 0, bhorse1)
        self.board.set_piece(6, 0, bhorse2)
        self.board.set_piece(2, 0, bbishop1)
        self.board.set_piece(5, 0, bbishop2)
        self.board.set_piece(3, 0, bqueen)
        self.board.set_piece(4, 0, bking)
    #method to move a piece
    def move_piece(self, x, y, piece):
        piece.move_piece(x, y, self.board)
    #printing the board with the correct formatting
    def print_board(self):
        for x in range(8):
            if x == 0:
                print(" ", "_"*81)
            print(x, "|",end= "")
            for y in range(8):

                if type(self.board.boardstate[y][x]) == Rook:
                    print("", self.board.boardstate[y][x], end="  |")
                elif type(self.board.boardstate[y][x]) == Horse:
                    print("", self.board.boardstate[y][x], end=" |")
                elif type(self.board.boardstate[y][x]) == Pawn:
                    print("", self.board.boardstate[y][x], end="  |")
                elif type(self.board.boardstate[y][x]) == King:
                    print(" ", self.board.boardstate[y][x], end="  |")
                elif type(self.board.boardstate[y][x]) == Queen:
                    print(" ", self.board.boardstate[y][x], end=" |")
                elif type(self.board.boardstate[y][x]) == Bishop:
                    print(self.board.boardstate[y][x], end=" |")
                else:
                    print("   ", self.board.boardstate[y][x], end="    |")

            print()
            print(" ","|_________"*8)
            if x == 7:
                    print("       0   ", "    1    ", "     2    ", "    3    ",
                          "    4    ", "    5    ", "    6    ", "    7    ")

#setting the game object
game = Game(board1)
game.set_game()
#function to run the game itself
def run_game(game):
    #help statement
    statement = "Welcome to the game. To move a piece simply follow the prompts given to you. \n" \
                "The game follows touch rules, meaning once you type a piece, you must move it. \n" \
                "After you have typed what you are prompted, press enter to keep playing\n" \
                "Please refrain from typing anything else.\n" \
                "For the pieces type the exact piece name(caps do not matter) \n" \
                "Make sure you input a move that is given to you. \n" \
                "To castle, please do it using the king. \n" \
                "Enjoy!"
    help = input("Hello! Welcome to this chess game. "
          "Press enter to start! "
          "For rules and instructions, please type help ").lower()
    if help == "help":
        print(statement)
    quitgame = False

    game.set_game()
    #loop that keeps on running until someone quits
    while quitgame != "q":
        game.print_board()

        turn = "w"
        piece = input("What piece do you want to move:    ").lower().strip()
        #converting the inputted piece into the piece object
        def convert_piece(piece):
            if piece == "wpawn1":
                piece = wpawn1
            elif piece == "wpawn2":
                piece = wpawn2
            elif piece == "wpawn3":
                piece = wpawn3
            elif piece == "wpawn4":
                piece = wpawn4
            elif piece == "wpawn5":
                piece = wpawn5
            elif piece == "wpawn6":
                piece = wpawn6
            elif piece == "wpawn7":
                piece = wpawn7
            elif piece == "wpawn8":
                piece = wpawn8
            elif piece == "bpawn1":
                piece = bpawn1
            elif piece == "bpawn2":
                piece = bpawn2
            elif piece == "bpawn3":
                piece = bpawn3
            elif piece == "bpawn4":
                piece = bpawn4
            elif piece == "bpawn5":
                piece = bpawn5
            elif piece == "bpawn6":
                piece = bpawn6
            elif piece == "bpawn7":
                piece = bpawn7
            elif piece == "bpawn8":
                piece = bpawn8
            elif piece == "wrook1":
                piece = wrook1
            elif piece == "wrook2":
                piece = wrook2
            elif piece == "brook1":
                piece = brook1
            elif piece == "brook2":
                piece = brook2
            elif piece == "whorse1":
                piece = whorse1
            elif piece == "whorse2":
                piece = whorse2
            elif piece == "bhorse1":
                piece = bhorse1
            elif piece == "bhorse2":
                piece = bhorse2
            elif piece == "wbishop1":
                piece = wbishop1
            elif piece == "wbishop2":
                piece = wbishop2
            elif piece == "bbishop1":
                piece = bbishop1
            elif piece == "bbishop2":
                piece = bbishop2
            elif piece == "wqueen":
                piece = wqueen
            elif piece == "bqueen":
                piece = bqueen
            elif piece == "wking":
                piece = wking
            elif piece == "bking":
                piece = bking
            else:
               pass
            return piece
        piece = convert_piece(piece)
        #making sure inputted piece is valid, or else an error will be raised
        while type(piece) == type(" "):
            print("Please input a valid piece name")
            piece = input("What piece do you want to move:    ").lower().strip()
            piece = convert_piece(piece)
        print(piece.valid_moves(game.board))

        xcord = input("What x position do you want to move it to:    ")
        ycord = input("What y position do you want to move it to:    ")
        convertedx = False
        convertedy = False
        #making sure inputted coordinates are correct
        while not convertedx:
            try:
                xcord = int(xcord)
            except:
                print("Input a valid coordinate from 0 - 7")
                xcord = input("What x position do you want to move it to:    ")
            if type(xcord) == type(6):
                if  xcord > 7 or xcord < 0:
                    print("Input a valid x coordinate from 0 - 7")
                    xcord = input("What x position do you want to move it to:    ")
                else:
                    convertedx = True
            else:
                convertedx == False
        while not convertedy:
            try:
                ycord = int(ycord)
            except:
                print("Input a valid coordinate from 0 -7")
                ycord = input("What y position do you want to move it to:    ")
            if type(ycord) == type(6):
                if  ycord > 7 or ycord < 0:
                    print("Input a valid y coordinate from 0 - 7")
                    ycord = input("What y position do you want to move it to:    ")
                else:
                    convertedy = True
            else:
                pass
        #executing the move, and continuing on
        game.move_piece(xcord, ycord, piece)
        quitgame = input("Press q to quit, press enter to continue.")

run_game(game)
