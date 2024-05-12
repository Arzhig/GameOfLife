import numpy as np
import matplotlib.pyplot as plt
from random import random
"""
class Cell:
    state:int=0
    def __init__(self,state:int=0):
        self.state = state
    def setLive(self):
        self.state = 1
    def setDead(self):
        self.state = 0
    def getState(self):
        return self.state

def setBoard(dimx:int=10,dimy:int=10):
    board = []
    for j in range(dimy):
        board.append([])
        for i in range(dimx):
            board[-1].append(Cell())
    board = np.array(board)
    return board

def randomizeBoard(board):
    for j in range(dimy):
        for i in range(dimx):
            seed = random()
            if seed <0.1:
                board[i,j].setLive()
    return board
"""
def setBoard(dimx:int=10,dimy:int=10):
    return np.zeros([dimx,dimy])

def randomizeBoard(board):
    dimx=board.shape[0]
    dimy=board.shape[1]
    for j in range(dimy):
        for i in range(dimx):
            seed = random()
            if seed <0.2:
                board[i,j] = 1
    return board

def getNumNei(board):
    dimx=board.shape[0]
    dimy=board.shape[1]
    padx = np.zeros(dimx)
    board = np.c_[padx,board,padx]
    pady = np.zeros(dimy + 2)
    board = np.r_[[pady],board,[pady]]
    values = np.zeros([dimx,dimy])
    for j in range(1,dimy+1):
        for i in range(1,dimx+1):
            values[i-1,j-1]=np.sum(board[i-1:i+2,j-1:j+2])-board[i,j]
    return values

def nextState(board):
    val = getNumNei(board)
    ind_new = val==3
    ind_dead = np.logical_or(val<2,val>3)
    board[ind_new]=1
    board[ind_dead]=0
    return board

board = randomizeBoard(setBoard(100,100))
print(board)
#print(getNumNei(board))

afig, ax = plt.subplots()

for i in range(5000):
    ax.clear()
    ax.imshow(board)
    ax.set_title(f"frame {i}")
    board = nextState(board)
    plt.pause(0.01)