from ChessPiece import Piece
from ChessQueen import Queen
from ChessBoard import Board

class Pawn(Piece):
    #methods to initialize variables and the return
    def __init__(self, piece, colour, startx, starty, img):
        super().__init__(piece, colour, startx, starty, img)
        self.first = True
        self.queen = False
        self.pawn = True
    def __str__(self):
        name = self.colour[0]+self.piece
        if self.queen:
            name = self.colour[0]+"Queen"
        return name
    #method checking and giving all valid moves
    def valid_moves(self, board):
        x = self.startx
        y = self.starty
        moves = []

        if y == 7 or y == 0:
            self.queen = True
        try:
            if self.colour == "Black":
                #the piece cannot move up if it is at the end
                if y < 7:
                    #if there is a piece in front of the pawn it can't do anything
                    if board.has_piece(x, y + 1):
                        pass
                    #if there is not a piece the pawn can move up
                    if not board.has_piece(x, y + 1):
                        moves.append([x, y + 1])
                    #if there is a piece to the diagnol, the pawn can move to capture
                    if x < 7:
                        if board.has_piece(x + 1, y + 1):
                            if board.which_piece(x + 1, y +1).colour != "Black":
                                moves.append([x + 1, y + 1])
                    if x > 0:
                        if board.has_piece(x - 1, y + 1):
                            if board.which_piece(x - 1, y +1).colour != "Black":
                                moves.append([x - 1, y + 1])
                    #if the piece is in it's first position, can move more
                    if self.first:
                        if board.has_piece(x, y + 1):
                            pass
                        else:
                            if board.has_piece(x, y + 2):
                                if board.which_piece(x, y + 2).colour != "Black":
                                    moves.append([x, y + 2])
                            else:
                                moves.append([x, y +2])
            #same for white
            else:
                if y > 0:
                    if board.has_piece(x, y - 1):
                        pass
                    if not board.has_piece(x, y - 1):
                        moves.append([x, y - 1])
                    if x < 7:
                        if board.has_piece(x + 1, y - 1):
                            if board.which_piece(x + 1, y - 1).colour != "White":
                                moves.append([x + 1, y - 1])
                    if x > 0:
                        if board.has_piece(x - 1, y - 1):
                            if board.which_piece(x - 1, y - 1).colour != "White":
                                moves.append([x - 1, y - 1])
                    if self.first:
                        if board.has_piece(x, y - 1):
                            pass
                        else:
                            if board.has_piece(x, y - 2):
                                if board.which_piece(x, y - 2).colour != "White":
                                    moves.append([x, y - 2])
                            else:
                                moves.append([x, y - 2])
            #If the pawn is promoted to a queen, it has new moves
            if self.queen:
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
                #top right
                cy = y - 1
                for i in range(x, 7):
                    if cy > -1:
                        if not board.has_piece(i + 1, cy):
                            moves.append([i + 1, cy])

                        else:
                            if board.which_piece(i + 1, cy).colour != self.colour:
                                moves.append([i + 1, cy])
                                break
                            else:
                                break
                    cy -= 1

                #top left
                cy = y-1
                cx = x-1

                for i in range(8):
                    if cy > -1 and cx > -1:
                        if not board.has_piece(cx, cy):
                            moves.append([cx, cy])
                        else:
                            if board.which_piece(cx, cy).colour != self.colour:
                                moves.append([cx, cy])
                                break
                            else:
                                break
                    cx -= 1
                    cy -= 1

                #bottom right
                cy = y +1
                cx = x +1
                for i in range(8):
                    if cy < 8 and cx < 8:
                        if not board.has_piece(cx, cy):
                            moves.append([cx, cy])
                        else:
                            if board.which_piece(cx, cy).colour != self.colour:
                                moves.append([cx, cy])
                                break
                            else:
                                break
                    cx += 1
                    cy += 1

                #bottom left
                cx = x - 1
                cy = y + 1
                for i in range(8):
                    if cy < 8 and cx > -1:
                        if not board.has_piece(cx, cy):
                            moves.append([cx, cy])
                        else:
                            if board.which_piece(cx, cy).colour != self.colour:
                                moves.append([cx, cy])
                                break
                            else:
                                break
                    cx -= 1
                    cy += 1
        except:
            pass
        return moves
