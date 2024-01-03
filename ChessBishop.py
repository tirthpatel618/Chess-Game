from ChessPiece import Piece
class Bishop(Piece):
    #inititalizing pieces and return
    def __init__(self, piece, colour, startx, starty, img):
        super().__init__(piece, colour, startx, starty, img)
    #method checking and giving all valid moves
    def valid_moves(self, board):
        x = self.startx
        y = self.starty
        moves = []
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

        return moves






