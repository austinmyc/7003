import random
import numpy as np

moves=[]
uppieces=["URC","URB","URA","ULA","ULB","ULC"]
downpieces=["DLC","DLB","DLA","DRA","DRB","DRC"]
#initialize board
board=np.array([["URC","URB","URA","ULA","ULB","ULC"],
                ["U","U","U","U","U","U"], 
                ["U","U","U","U","U","U"],
                ["D","D","D","D","D","D"],
                ["D","D","D","D","D","D"],
                ["DLC","DLB","DLA","DRA","DRB","DRC"]] )
record=[]
def main():
    global uppieces
    global downpieces
    global board     
    print(board)
    print()

    #while True:  
    for i in range(20) :
        upmove=uppieces[random.randint(0,len(uppieces)-1)]
        Umove(upmove)
        downmove=downpieces[random.randint(0,len(downpieces)-1)]
        Dmove(downmove)
        check_takeout()
        print(f"done move {i+1}")
        print_moves()
        print(board)
        check_win(board)
        check_end()
    #moving in same location logic
    
    
    
    
    

def Umove(piece):
    #Up move a piece down
    global board
    row, col = np.where(board==piece)
    row,col=row[0],col[0]
    if row!=5 and (board[row+1,col]=='U' or board[row+1,col]=='D'):
        board[row,col]="U"
        board[row+1,col]=piece
        record_moves(piece)
        #'X' denotes piece picked but no movement
    else: record_moves(piece+"X")
 
def Dmove(piece):
    #Down move a piece up
    global board
    row, col = np.where(board==piece)
    row,col=row[0],col[0]
    if row!=0 and (board[row-1,col]=="U" or board[row-1,col]=="D"):
        board[row,col]="D"
        board[row-1,col]=piece
        record_moves(piece)
    else: record_moves(piece+"X")

def check_takeout():
    global board
    global uppieces
    global downpieces
    temptakeout=[]
    tempuppieces=uppieces[:]
    tempdownpieces=downpieces[:]
    #A pieces check take out pieces
    for i in uppieces:
        row, col = np.where(board==i)
        row,col=row[0],col[0]
        try:
            if i=="URA":
                if board[row+1,col-1]=="DLB":
                    temptakeout.append([row+1,col-1])
                    tempdownpieces.remove("DLB")
                elif board[row+1,col+1]=="DRA":
                    temptakeout.append([row+1,col+1])
                    tempdownpieces.remove("DRA")
        except: None
        try:
            if i=="ULA":
                if board[row+1,col-1]=="DLA":
                    temptakeout.append([row+1,col-1])
                    tempdownpieces.remove("DLA")
                elif board[row+1,col+1]=="DRB":
                    temptakeout.append([row+1,col+1])
                    tempdownpieces.remove("DRB")
        except: None
        try:
            if i=="URA":
                if board[row+1,col-1]=="DLB":
                    temptakeout.append([row+1,col-1])
                    tempdownpieces.remove("DLB")
                elif board[row+1,col+1]=="DRA":
                    temptakeout.append([row+1,col+1])
                    tempdownpieces.remove("DRA")
        except: None
    for i in downpieces:
        row, col = np.where(board==i)
        row,col=row[0],col[0]
        try:
            if i=="DLA":
                if board[row-1,col-1]=="URB":
                    temptakeout.append([row+1,col-1])
                    tempuppieces.remove("URB")
                elif board[row-1,col+1]=="ULA":
                    temptakeout.append([row-1,col+1])
                    tempuppieces.remove("ULA")
        except: None
        try:
            if i=="DRA":
                if board[row-1,col-1]=="URA":
                    temptakeout.append([row+1,col-1])
                    tempuppieces.remove("URA")
                elif board[row-1,col+1]=="ULB":
                    temptakeout.append([row-1,col+1])
                    tempuppieces.remove("ULB")
        except: None
    #B pieces check take out indices


    #C pieces check take out indices
    for i in temptakeout:
        print("i:", i)
        print(board[*i])
        if board[*i] not in tempuppieces:
            board[*i]="U"
        if board[*i] not in tempdownpieces:
            board[*i]="D"
    print("checktakeout\n",board)
    downpieces=tempdownpieces[:]
    print("downpieces",downpieces)
    uppieces=tempuppieces[:]
    print("uppieces",uppieces)

def check_win(board):
    upwins=[]
    for i in downpieces:
        upwins.append(any(i in sublist for sublist in board))
    if not any(upwins):
        print("Up wins")

    downwins=[]
    for i in uppieces:
        downwins.append(any(i in sublist for sublist in board))
    if not any(downwins):
        print("Down wins")

def check_end():
    ...

def record_moves(piece):
    global record
    record.append(piece)

def print_moves():
    global record
    reshaped = [record[i: i + 2] + [None] * (i + 2 - len(record)) for i in range(0, len(record), 2)]
    print(f"Moves record: {reshaped}")


if __name__ == "__main__":
    main()