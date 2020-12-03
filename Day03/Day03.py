import sys
import math
sys.path.append('./')
from adventInput import GetInput

_input = GetInput(3)

height = len(_input)
width = len(_input[0])

slopes = {
  'xSlopes': [1,3,5,7,1], 'ySlopes':[1,1,1,1,2]
}

iterator = 0
treesList = []

while iterator < len(slopes['xSlopes']):
  rowCurrent = 0
  colCurrent = 0
  xSlope = slopes["xSlopes"][iterator]
  ySlope = slopes["ySlopes"][iterator]
  trees = 0
  while True:
    column = (rowCurrent + xSlope) % width
    row = (colCurrent + ySlope)
    if row >= height:
      break

    if _input[row][column] == "#":
      trees+= 1
    
    rowCurrent = column
    colCurrent = row
  if xSlope == 3 and ySlope == 1:
    print(trees)
  treesList.append(trees)
  iterator+= 1


sumTrees = 1
for x in treesList:
  sumTrees *= x

print(sumTrees)