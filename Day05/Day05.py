import sys
import math
import time
sys.path.append('./')
from adventInput import GetInput

_input = GetInput(5)
seatIds = []

def BinarySearch(tree, index, low, high):
  if index >= len(tree):
    return low
  currentDirection = tree[index]
  index += 1

  mid = (high + low + 1) // 2
  
  if currentDirection == "F" or currentDirection == "L":
    return BinarySearch(tree, index, low, mid)

  elif currentDirection == "B" or currentDirection == "R":
    return BinarySearch(tree, index, mid, high)
  

def GetAllSeatIdsRecursion():
  now = time.time()
  for line in _input:
    rowTree = line[0:7]
    columnTree = line[-3:]

    row = BinarySearch(rowTree, 0, 0, 127)
    col = BinarySearch(columnTree, 0, 0, 7)

    seatId = row * 8 + col
    seatIds.append(seatId)

  end = time.time()

  print(end - now)

def GetAllSeatIdsByConvertingToBinary():
  now2 = time.time()
  for line in _input:
    rowTree = line[0:7]
    columnTree = line[-3:]
    rowTree = rowTree.replace('B', '1').replace('F', '0')
    columnTree = columnTree.replace('R', '1').replace('L', '0')

    #dont need leading zero because bytes are leading 0 by default
    row = int(rowTree, 2)
    col = int(columnTree, 2)

    seatId = row * 8 + col
    seatIds.append(seatId)

  end2 = time.time()
  print(end2 - now2)

def FindMySeat():
  sortedSeats = sorted(seatIds)
  combinations = zip(sortedSeats[1:], sortedSeats)
  for (nextSeat, currentSeat) in combinations:
    if nextSeat - currentSeat != 1:
      print(currentSeat + 1)


GetAllSeatIdsRecursion()

seatIds.clear()

GetAllSeatIdsByConvertingToBinary()

print(max(seatIds))

FindMySeat()
