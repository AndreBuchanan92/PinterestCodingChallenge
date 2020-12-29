# Do not remove these imports. You may add others if you wish.
import sys
import numpy as np 

# Args:
#   board: a list of list of strings, each list is a row of the board.
#          Each string will be "+" for impassable squares, and "0" for
#          squares the snake can move through.
#   row: an integer, the row the snake will start on
#   col: an integer, the column the snake will start on
#
# Returns:
#   A tuple of two ints, (row, col), the closest edge square the snake can exit.
#   If multiple are equally close, the one with smallest row value. If there
#   are multiple with smallest row value, the one with smallest column value.
#   If there are no answers, return (-1, -1)

def checkHistory(row, col, history):
    exist = False
    for (i, j) in history:
        if row == i and col == j:
            exist = True
            break
            
    return exist
       
def isEdge(board, row, col):
    height = len(board)
    width = len(board[0])
    
    if row == 0 or row == height - 1:
        return True
    
    if col == 0 or col == width - 1:
        return True
    
    return False
  
def isValidPos(board, row, col):
    height = len(board)
    width = len(board[0])
    if row < 0 or row >= height:
        return False
      
    if col < 0 or col >= width:
        return False
      
    if board[row][col] == '+':
        return False
      
    return True
          
def move_snake(board, row, col, history, sol, start_flag):      
    if isValidPos(board, row, col) == False: # invalid pos        
        return sol
      
    if checkHistory(row, col, history) == True: # check if already passed
        # print('checkHistory', row, col)
        return sol
    
    if isEdge(board, row, col) == True and start_flag == False: # exit
        len1 = len(history)
        # print('Edge', row, col, len1, sol[2])
        if len1 > sol[2]:
            return sol
        
        if len1 < sol[2]: # compare length
            return (row, col, len1)            
        elif row < sol[0]: # compare row
            return (row, col, len1)
        elif col < sol[1]: # compare column
            return (row, col, len1)
            
        return sol
        
    history.append((row, col))
    # print('Move', row, col, len(history))
    
    # left    
    sol = move_snake(board, row, col - 1, history, sol, False)
    
    # right
    sol = move_snake(board, row, col + 1, history, sol, False)
        
    # top
    sol = move_snake(board, row - 1, col, history, sol, False)
    
    # bottom
    sol = move_snake(board, row + 1, col, history, sol, False)
    
    history.pop()
    
    return sol
    
  
def find_exit(board, row, column):    
    count = len(board) * len(board[0])
    sol = (-1, -1, count)
    
    # Your code goes here    
    history = []
    sol = move_snake(board, row, column, history, sol, True)
    
    return (sol[0], sol[1])
    
    

#Write a function that takes a rectangular board with only +’s and 0’s, along with a starting point on the edge of the board (given row first, then column), and returns the coordinates of the nearest exit to which it can travel.

#If multiple exits are equally close, give the one with the lowest numerical value for the row. If there is still a tie, give the one of those with the lowest numerical value for the column.

#If there is no answer, output -1 -1

#The board will be non-empty and rectangular. All values in the board will be either + or 0. All coordinates (input and output) are zero-based. All start positions will be 0, and be on the edge of the board. For example, (0,0) would be the top left corner of any size input.


  # NOTE: You may use print statements for debugging purposes, but you may
  #       need to remove them for the tests to pass.
  

# DO NOT MODIFY BELOW THIS LINE
def main():
  start = None
  board = []

  for line in sys.stdin:
    if len(line.strip()) == 0:
      continue

    if start is None:
      start = tuple(int(x) for x in line.rstrip().split(" "));
    else:
      board.append(line.rstrip().split(" "))

  print(" ".join(str(x) for x in find_exit(board, *start)))

main()
