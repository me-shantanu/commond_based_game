import numpy as np



ROW_C = 6
COL_C =7

def create():
    bor = np.zeros((ROW_C,COL_C))
    return bor

def dropp( bor, row,selection,piece):
    bor[row][selection] = piece

    


def is_valide(bor, selection):
    return bor[ROW_C-1][selection] == 0

def get_next_open(bor, selection):
    for r in range(ROW_C):
        if bor[r][selection] == 0:
            return r

def pbor(bor):
    print(np.flip(bor, 0))

def winning_move(bor,piece):
    # check all the horigential location
    for c in range(COL_C-3):
        for r in range(ROW_C):
            if bor[r][c] == piece and bor[r][c+1] == piece  and bor[r][c+2] == piece and bor[r][c+3] == piece:
                return True
    # check all the vertical location
    for c in range(COL_C):
        for r in range(ROW_C-3):
            if bor[r][c] == piece and bor[r+1][c] == piece  and bor[r+2][c] == piece and bor[r+3][c] == piece:
                return True
# possitivly sloped sloped digonal
    for c in range(COL_C-3):
        for r in range(ROW_C-3):
            if bor[r][c] == piece and bor[r+1][c+1] == piece  and bor[r+2][c]+2 == piece and bor[r+3][c+3] == piece:
                return True


#check negativly sloped digonal
    for c in range(COL_C-3):
        for r in range(3,ROW_C):
            if bor[r][c] == piece and bor[r-1][c+1] == piece  and bor[r-2][c]+2 == piece and bor[r-3][c+3] == piece:
                return True

bor = create()

print (pbor(bor))
game_over = False
turn = 0


while not game_over:
    #ask1 player to input
    if turn == 0:
        selection = int(input("player one selecte between 0-6 : "))

        if is_valide(bor, selection):
            row = get_next_open(bor, selection)
            dropp(bor, row, selection,1)
            if winning_move(bor, 1):
                print("player one won ! congrats")
                game_over = True

    #ask player to input
    else: 
        selection = int(input("player two selecte between 0-6 : "))
        if is_valide(bor, selection):
            row = get_next_open(bor, selection)
            dropp(bor, row, selection,2)
            if winning_move(bor, 2):
                print("player two won ! congrats")
                game_over = True
        

    pbor(bor)
    turn += 1
    turn = turn % 2

