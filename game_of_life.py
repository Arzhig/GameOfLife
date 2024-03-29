import time
import random

def dead_state(row,col):
  state = [[0 for i in range(col)] for i in range(row)]
  return state

def random_state(row, col):
  state =  dead_state(row, col)
  for i in range(len(state)):
    for j in range(len(state[i])):
      rd = random.random()
      if rd > 0.5:
        state[i][j] = 1
      else :
        state[i][j] = 0
  return state

def render(state):
  endstr = ""
  endstr += "_"*(len(state[0])+4) + '\n'
  for row in state:
    row_str = '| '
    for cell in row:
      if cell == 0:
        row_str += ' '
      else:
        row_str += '#'
    row_str += ' |'
    endstr += row_str + '\n'
  endstr += "_"*(len(state[0])+4)
  return endstr

def next_state(state):
  new_state = [[cell for cell in row] for row in state]
  for i in range(len(state)):
    for j in range(len(state[i])):

      if i==0:

        if j==0:

          if state[i][j+1] + state[i+1][j+1] + state[i+1][j] <= 1:
            new_state[i][j]=0
          elif state[i][j+1] + state[i+1][j+1] + state[i+1][j] == 3:
            new_state[i][j]=1

        elif j==len(state[i])-1:
          if state[i][j-1] + state[i+1][j-1] + state[i+1][j] <= 1:
            new_state[i][j]=0
          elif state[i][j-1] + state[i+1][j-1] + state[i+1][j] == 3:
            new_state[i][j]=1

        else :
          if state[i][j-1] + state[i][j+1] + state[i+1][j-1] + state[i+1][j+1] + state[i+1][j] <= 1 or state[i][j-1] + state[i][j+1] + state[i+1][j-1] + state[i+1][j+1] + state[i+1][j] >=4 :
            new_state[i][j] = 0
          elif state[i][j-1] + state[i][j+1] + state[i+1][j-1] + state[i+1][j+1] + state[i+1][j] == 3 :
            new_state[i][j] = 1

      elif i == len(state)-1:
        if j==0:

          if state[i][j+1] + state[i-1][j+1] + state[i-1][j] <= 1:
            new_state[i][j]=0
          elif state[i][j+1] + state[i-1][j+1] + state[i-1][j] == 3:
            new_state[i][j]=1

        elif j==len(state[i])-1:
          if state[i][j-1] + state[i-1][j-1] + state[i-1][j] <= 1:
            new_state[i][j]=0
          elif state[i][j-1] + state[i-1][j-1] + state[i-1][j] == 3:
            new_state[i][j]=1

        else :
          if state[i][j-1] + state[i][j+1] + state[i-1][j-1] + state[i-1][j+1] + state[i-1][j] <= 1 or state[i][j-1] + state[i][j+1] + state[i-1][j-1] + state[i-1][j+1] + state[i-1][j] >=4 :
            new_state[i][j] = 0
          elif state[i][j-1] + state[i][j+1] + state[i-1][j-1] + state[i-1][j+1] + state[i-1][j] == 3 :
            new_state[i][j] = 1

      else :
        if j==0:

          if state[i-1][j] + state[i-1][j+1] + state[i][j+1] + state[i+1][j+1] + state[i+1][j] <= 1 or state[i-1][j] + state[i-1][j+1] + state[i][j+1] + state[i+1][j+1] + state[i+1][j] >=4 :
            new_state[i][j] = 0
          elif state[i-1][j] + state[i-1][j+1] + state[i][j+1] + state[i+1][j+1] + state[i+1][j] == 3 :
            new_state[i][j] = 1

        elif j==len(state[i])-1:
          if state[i-1][j] + state[i-1][j-1] + state[i][j-1] + state[i+1][j-1] + state[i+1][j] <= 1 or state[i-1][j] + state[i-1][j-1] + state[i][j-1] + state[i+1][j-1] + state[i+1][j] >=4 :
            new_state[i][j] = 0
          elif state[i-1][j] + state[i-1][j-1] + state[i][j-1] + state[i+1][j-1] + state[i+1][j] == 3 :
            state[i][j] = 1

        else :
          if state[i-1][j] + state[i-1][j+1] + state[i][j+1] + state[i+1][j+1] + state[i+1][j] + state[i+1][j-1] + state[i][j-1] + state[i-1][j-1] <= 1 or state[i-1][j] + state[i-1][j+1] + state[i][j+1] + state[i+1][j+1] + state[i+1][j] + state[i+1][j-1] + state[i][j-1] + state[i-1][j-1] >=4 :
            new_state[i][j] = 0
          elif state[i-1][j] + state[i-1][j+1] + state[i][j+1] + state[i+1][j+1] + state[i+1][j] + state[i+1][j-1] + state[i][j-1] + state[i-1][j-1] == 3 :
            new_state[i][j] = 1

  return new_state

state = random_state(10,10)
render(state)
render(next_state(state))
render(next_state(next_state(state)))

state = random_state(55,700)
i=0
while i < 10000 :
  time.sleep(0.1)
  i+=1
  print(render(state))
  state=next_state(state)

