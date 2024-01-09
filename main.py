import random
import os
import time

BOARD_CHAR = [' ', '*']

def createBoard(row, col): 
  arr = []
  for i in range(row):
    arr.append([])
    for j in range(col):
      arr[i].append(0)

  return arr
def nextState(board):
  ROW = len(board)
  COL = len(board[0])

  buffer = [[0 for i in range(COL)] for i in range(ROW)]

  for r in range(ROW):
      for c in range(COL):
          total = 0
          upper_r, lower_r = min(r + 2, ROW), max(r - 1, 0)
          upper_c, lower_c = min(c + 2, COL), max(c - 1, 0)


          for i in range(lower_r, upper_r):
              for j in range(lower_c, upper_c):
                  total += board[i][j]

          total -= board[r][c]


          if (total == 2 or total == 3) and board[r][c] == 1:
              buffer[r][c] = 1
          elif total == 3:
              buffer[r][c] = 1

  for r in range(ROW):
      for c in range(COL):
          board[r][c] = buffer[r][c]     
def randomStartState(board, n = 10):
  ROW = len(board)
  COL = len(board[0])
  
  for _ in range(n):
    x = random.randrange(0, ROW)
    y = random.randrange(0, COL)

    board[x][y] = 1  
def displayBoard(board):
  ROW = len(board)
  COL = len(board[0])
  
  for i in range(ROW):
    for j in range(COL):
      if board[i][j] == 0:
        print(BOARD_CHAR[0], end='')
      else:
        print(BOARD_CHAR[1], end='')
    print()
  print()
  
def main():
  board = createBoard(50, 50)
  randomStartState(board, n = 1000)
  
  while True:
    nextState(board)
    displayBoard(board)
    time.sleep(0.5)
    os.system('cls' if os.name == 'nt' else 'clear')

if '__main__' == __name__:
  main()