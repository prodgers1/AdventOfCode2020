import sys
import math
import time
sys.path.append('./')
from adventInput import GetInput
import copy
import itertools
import collections

_input = GetInput(10)

intInput = [int(i) for i in _input]
intInput.append(0)
sortedInput = sorted(intInput)

highestJolt = sortedInput[-1] + 3

oneJoltDifference = 0
threeJoltDifference = 1


for i in range(len(sortedInput) -1):
  difference = sortedInput[i+1] - sortedInput[i]
  if difference == 1:
    oneJoltDifference += 1
  elif difference == 3:
    threeJoltDifference += 1

print (oneJoltDifference * threeJoltDifference)

allTheLists = list()
calculatedCombos = {}

def findCombinationsAddToList(lines, currentIndex, newList):
  if currentIndex == len(lines) - 1:
    allTheLists.append(list(newList))
    
  for nextIndex in range(currentIndex+1, len(lines)):
    if lines[nextIndex] - lines[currentIndex] <= 3:
      newList.append(lines[nextIndex])
      findCombinationsAddToList(lines, nextIndex, newList)
      #once the subchildren are done with all the combinations, pop off the last element found, which will allow you to 
      # now try all the combinations of the previous element and then back to the leaf nodes
      #easy way to get all the combinations of the subchildren
      newList.pop()


#this recursive function's goal is to find all of the distinct combinations in a MASSIVE tree.
# When we walk all the way to the bottom, we know how many distinct combinations are beneath the current node
# by saving that in a dictionary where the key is the node value, and the value is the number of distinct combos beneath the node,
# we never have to trace our steps again. And by keeping track of where we have been, we reduce the search space DRAMATICALLY.
# Whats nice is you code this as the brute force solution, then just add the optimizations afterwards of keeping track of where you have been
def findCombinations(lines, currentIndex):
  currentDistinctCombos = 0

  if currentIndex == len(lines) -1:
    return 1

  if currentIndex in calculatedCombos:
    return calculatedCombos[currentIndex]

  for nextIndex in range(currentIndex+1, len(lines)):
    if lines[nextIndex] - lines[currentIndex] <= 3:
      currentDistinctCombos += findCombinations(lines, nextIndex)
      
  calculatedCombos[currentIndex] = currentDistinctCombos
  return currentDistinctCombos

distinctCombos = findCombinations(sortedInput, 0)
#findCombinationsAddToList(sortedInput, 0, [])
print(distinctCombos)


