import random
import os

def printingboard(board):
    for row in board:
        for item in row:
            if item=='1':
                print('❌', end=' ')
            elif item == '2':
                print('⭕️',end=' ')
            else:
                print(item,end=' ')
        print()
def horizontalcheck(board):
    win = 3
    for row in board:
        if row[0] == row[1] == row[2]:
            win = row[0]
            break
    return win
def verticalcheck(board):
    win = 3
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col]:
            win = board[0][col]
            break
    return win
def diagonalcheck(board):
    win = 3
    if board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    
    if board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]
    
    return None 
def winner(board):
    win = horizontalcheck(board)
    if win != '1' and win != '2':
        win = verticalcheck(board)
        if win != '1' and win != '2':
            win = diagonalcheck(board)
            if win != '1' and win != '2':
                return None
    return win
def comp_move(board, pos_avail):
    move = '0'
    if ('22' in pos_avail):
        move = '22'
    elif('11' in pos_avail):
        move = '11'
    elif('13' in pos_avail):
        move = '13'
    elif('31' in pos_avail):
        move = '31'
    elif('33' in pos_avail):
        move = '33'
    else:
        move = random.choice(pos_avail)
    
    return move
    
board = [['🟥','🟥','🟥']
         ,['🟥','🟥','🟥']
         ,['🟥','🟥','🟥']]

positions_available = ['11','12','13','21','22','23','31','32','33',]
win = 0

printingboard(board)


print("enter row and column in format of rc e.g: 31 this means 3rd row and first column")

while(board):
    
    position = input("enter position: ")
    os.system('cls')
    
    if(position in positions_available):
    
        positions_available.remove(position)
        r = int(position[0])
        c = int(position[1])
        board[r-1][c-1] = '1'
        
        win = winner(board)
        if(win=='1'):
            print("✅✅✅✅ Ⓨ Ⓞ Ⓤ  Ⓦ Ⓘ Ⓝ  ✅✅✅✅")
            break
        elif(win=='2'):
            print("⛔️⛔️⛔️⛔️ Ⓨ Ⓞ Ⓤ  Ⓛ Ⓞ Ⓢ Ⓔ ⛔️⛔️⛔️⛔️")
            break
        
    
        comp_pos = comp_move(board, positions_available)
        positions_available.remove(comp_pos)
        r = int(comp_pos[0])
        c = int(comp_pos[1])
        board[r-1][c-1] = '2'
        
        

        printingboard(board)
    
    
    
    elif(position is not positions_available):
        print('already filled portion before please try again')
    else:
        print("wrong choice!")



printingboard(board)
    
    
    
    




