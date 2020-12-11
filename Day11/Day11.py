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

def checkAdjacent(rowIndex, colIndex):
  occupied = 0

  if rowIndex + 1 < rowLength:
    down = _originalInput[rowIndex + 1][colIndex]
    if down == '#':
      occupied += 1
  
  if rowIndex + 1 < rowLength and colIndex + 1 < colLength:
    downRight = _originalInput[rowIndex + 1][colIndex + 1]
    if downRight == '#':
      occupied += 1
  
  if rowIndex + 1 < rowLength and colIndex - 1 >= 0:
    downLeft = _originalInput[rowIndex + 1][colIndex - 1]
    if downLeft == '#':
      occupied += 1
  
  if colIndex - 1 >= 0:
    left = _originalInput[rowIndex][colIndex-1]
    if left == '#':
      occupied += 1
  
  if rowIndex - 1 >= 0:
    up = _originalInput[rowIndex -1][colIndex] 
    if up == '#':
      occupied += 1
  
  if rowIndex - 1 >= 0 and colIndex - 1 >= 0:
    upLeft = _originalInput[rowIndex - 1][colIndex - 1]
    if upLeft == '#':
      occupied += 1

  if rowIndex - 1 >= 0 and colIndex + 1 < colLength:
    upRight = _originalInput[rowIndex - 1][colIndex + 1]
    if upRight == '#':
      occupied += 1
  
  if colIndex + 1 < colLength:
    right = _originalInput[rowIndex][colIndex +1]
    if right == '#':
      occupied += 1
  
  return (occupied == 0, occupied >= 4)

def reset(rowIndex, colIndex):
  return (rowIndex, colIndex)

def findNextAvailableSeat(rowIndex, colIndex):
  occupied = 0
  localRow, localCol = reset(rowIndex, colIndex)
  while localRow + 1 < rowLength:
    down = _originalInput[localRow + 1][localCol]
    if down == '#':
      occupied += 1
      break
    elif down == 'L':
      break
    else:
      localRow += 1

  localRow, localCol = reset(rowIndex, colIndex)
  while localRow + 1 < rowLength and localCol + 1 < colLength:
    downRight = _originalInput[localRow + 1][localCol + 1]
    if downRight == '#':
      occupied += 1
      break
    elif downRight == 'L':
      break
    else:
      localRow += 1
      localCol += 1
  
  localRow, localCol = reset(rowIndex, colIndex)
  
  while localRow + 1 < rowLength and localCol - 1 >= 0:
    downLeft = _originalInput[localRow + 1][localCol - 1]
    if downLeft == '#':
      occupied += 1
      break
    elif downLeft == 'L':
      break
    else:
      localRow += 1
      localCol -= 1 

  localRow, localCol = reset(rowIndex, colIndex)
  while localCol - 1 >= 0:
    left = _originalInput[localRow][localCol-1]
    if left == '#':
      occupied += 1
      break
    elif left == 'L':
      break
    else:
      localCol -= 1
  
  localRow, localCol = reset(rowIndex, colIndex)
  while localRow - 1 >= 0:
    up = _originalInput[localRow -1][localCol] 
    if up == '#':
      occupied += 1
      break
    elif up == 'L':
      break
    else:
      localRow -= 1
      
  localRow, localCol = reset(rowIndex, colIndex)
  while localRow - 1 >= 0 and localCol - 1 >= 0:
    upLeft = _originalInput[localRow - 1][localCol - 1]
    if upLeft == '#':
      occupied += 1
      break
    elif upLeft == 'L':
      break
    else:
      localRow -= 1
      localCol -= 1

  localRow, localCol = reset(rowIndex, colIndex)
  while localRow - 1 >= 0 and localCol + 1 < colLength:
    upRight = _originalInput[localRow - 1][localCol + 1]
    if upRight == '#':
      occupied += 1
      break
    elif upRight == 'L':
      break
    else:
      localRow -= 1
      localCol += 1

  localRow, localCol = reset(rowIndex, colIndex)
  while localCol + 1 < colLength:
    right = _originalInput[localRow][localCol +1]
    if right == '#':
      occupied += 1
      break
    elif right == 'L':
      break
    else:
      localCol += 1
  
  return (occupied == 0, occupied >= 5)

changed = True
while changed:
  changed = False
  inputToChange = copy.deepcopy(_originalInput)
  for rowIndex, row in enumerate(_originalInput):
    for colIndex, col in enumerate(row):
      if _originalInput[rowIndex][colIndex] == '.':
        continue
      if _originalInput[rowIndex][colIndex] == 'L' or _originalInput[rowIndex][colIndex] == '#':
        (noOccupied, fourOrMoreOccupied) = findNextAvailableSeat(rowIndex, colIndex);  

        if noOccupied and _originalInput[rowIndex][colIndex] == 'L':
          changed = True
          inputToChange[rowIndex][colIndex] = '#'
        
        elif fourOrMoreOccupied and _originalInput[rowIndex][colIndex] == '#':
          changed = True
          inputToChange[rowIndex][colIndex] = 'L'

  _originalInput = copy.deepcopy(inputToChange)


occupiedSeats = 0
for i, row in enumerate(_originalInput):
  for j, col in enumerate(row):
    if _originalInput[i][j] == '#':
      occupiedSeats += 1
    
print (occupiedSeats)
  