import sys
import math
import time
sys.path.append('./')
from adventInput import GetInput
import copy
import itertools
import collections

_input = GetInput(11)
_input = [list(r) for r in _input]
_originalInput = copy.deepcopy(_input)
rowLength = len(_input)
colLength = len(_input[0])


def checkAdjacent(rowIndex, colIndex, grid):
  occupied = 0

  for dr in [-1,0,1]:
    for dc in [-1,0,1]:
      if dr == 0 and dc == 0:
        continue
      rowPlusOffset = rowIndex + dr
      colPlusOffset = colIndex + dc

      if (0 <= rowPlusOffset < rowLength and 0 <= colPlusOffset < colLength and grid[rowPlusOffset][colPlusOffset] == '#'):
        occupied += 1
 
  return (occupied == 0, occupied >= 4)

def findNextAvailableSeat(rowIndex, colIndex, grid):
  occupied = 0
  # by checking the change in the row and the change in the column, this gets me every adjacent direction around the current row/col index
  # by using two more for loops, im able to save a ton of if checking, and now all i have to worry about is if im lower than 0 or greater than
  # the length of the row or column
  # The only difference from part 1 is i needed to look indefinitely in the direction i was going to find a seat, and only when it was a floor (.)
  # look past it, and see if there is ever an occupied seat.
  for dr in [-1,0,1]:
    for dc in [-1,0,1]:
      if dr == 0 and dc == 0:
        continue
      rowPlusOffset = rowIndex + dr
      colPlusOffset = colIndex + dc
      while 0 <= rowPlusOffset < rowLength and 0 <= colPlusOffset < colLength and grid[rowPlusOffset][colPlusOffset] == '.':
        rowPlusOffset = rowPlusOffset + dr
        colPlusOffset = colPlusOffset + dc
        
      if 0 <= rowPlusOffset < rowLength and 0 <= colPlusOffset < colLength and grid[rowPlusOffset][colPlusOffset] == '#':
        occupied += 1
  
  return (occupied == 0, occupied >= 5)

def run(grid, part1):
  changed = True
  while changed:
    changed = False
    inputToChange = copy.deepcopy(grid)
    for rowIndex, row in enumerate(grid):
      for colIndex, col in enumerate(row):

        if grid[rowIndex][colIndex] == 'L' or grid[rowIndex][colIndex] == '#':
          if part1:
            (noOccupied, fourOrMoreOccupied) = checkAdjacent(rowIndex, colIndex, grid);    
          else:
            (noOccupied, fourOrMoreOccupied) = findNextAvailableSeat(rowIndex, colIndex, grid);  

          if noOccupied and grid[rowIndex][colIndex] == 'L':
            changed = True
            inputToChange[rowIndex][colIndex] = '#'
          
          elif fourOrMoreOccupied and grid[rowIndex][colIndex] == '#':
            changed = True
            inputToChange[rowIndex][colIndex] = 'L'

    grid = copy.deepcopy(inputToChange)
  
  occupiedSeats = 0
  for i, row in enumerate(grid):
    for j, col in enumerate(row):
      if grid[i][j] == '#':
        occupiedSeats += 1
  print (occupiedSeats)

run(_originalInput, True)
run(_originalInput, False)
    
  