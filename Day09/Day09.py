import sys
import math
import time
sys.path.append('./')
from adventInput import GetInput
import copy
import itertools
import collections

_input = GetInput(9)

preambleSize = 25
startIndex = 0

endIndex = preambleSize

while True:
  currentPreamble =  _input[startIndex:endIndex] 
  if endIndex + 1 >= len(_input):
    break

  target = int(_input[endIndex])
  valid = False
  for c in currentPreamble:
    toFind = target - int(c)
    if str(toFind) in currentPreamble:
      valid = True
      break
      
  if not valid:
    print(target)
    break
  
  startIndex += 1
  endIndex += 1

target = 10884537

i = 0
for current in _input:
  
  currentSum = 0
  tried = list()
  offset = 0
  while currentSum < target:
    toAdd = _input[i+offset]
    currentSum += int(toAdd)
    tried.append(toAdd)
    offset += 1
  
  i+=1

  if currentSum == target:
    sortedList = sorted(tried)
    print(int(sortedList[0]) + int(sortedList[-1]))
    break

