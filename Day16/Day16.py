import sys
import math
import time
sys.path.append('./')
from adventInput import GetInput
import copy
import itertools
import collections


def findAttributes(rules, slices):
  columnMap = {}

  while len(columnMap) != len(rules):
    newValues = {}
    for key, values in slices.items():
      potentials = []
      for ruleName, validRanges in rules.items():
        if ruleName not in columnMap:
          valid = True
          for value in values:
            if value in validRanges:
              continue
            else:
              valid = False
              break
          
          if valid:
            potentials.append(ruleName)
      if len(potentials) == 1:
        columnMap[potentials[0]] = key
      else:
        newValues[key] = values
    slices = newValues
  
  return columnMap

_input = GetInput(16)
indicies = [i for i, x in enumerate(_input) if x == '']
notes = {}

for i in range(0, indicies[0]):
  line = _input[i] 
  name, values = line.split(':')
  firstValue, _, secondValue = values.split()
  
  first,last = firstValue.split('-')
  secondFirst, secondLast = secondValue.split('-')
  
  firstList = list(range(int(first), int(last)+1))
  secondList = list(range(int(secondFirst), int(secondLast)+1))
  notes[name] = firstList + secondList
  
#gets nearby tickets:
invalidTickets = list()
invalidSeatNumbers = list()
allTickets = list()
for i in range(indicies[-1]+2, len(_input)):
  line = _input[i].split(',')
  allTickets.append(line)

  for j in line:
    valid = False
    for k in notes.values():
      if int(j) in k:
        valid = True
        break
    
    if not valid:
      invalidSeatNumbers.append(int(j))
      invalidTickets.append(line)

print(sum(invalidSeatNumbers))

validTickets = []

for ticket in allTickets:
  if ticket not in invalidTickets:
    validTickets.append(ticket)

positions = list()
availablePositions = [key for key in notes.keys()]

verticalSlices = {}
for i in range(len(validTickets[0])):
  numsToCheck = list()
  ap = list(availablePositions)
  for j in range(len(validTickets)):
    numToCheck = validTickets[j][i]
    numsToCheck.append(int(numToCheck))

  verticalSlices[i] = numsToCheck

columnMap = findAttributes(notes, verticalSlices)

myTicket = _input[indicies[0]+2]

myTicketNums = myTicket.split(',')

myTicketDict = {}

ans = 1
for ruleName, indexOfRule in columnMap.items():
  if "departure" in ruleName:
    ans *= int(myTicketNums[indexOfRule])

print(ans)