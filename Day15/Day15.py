import sys
import math
import time
sys.path.append('./')
from adventInput import GetInput
import copy
import itertools
import collections

_input = "2,0,1,7,4,14,18"

_testInput = "2,0,1,7,4,14,18"

_input = _testInput

_input = _input.split(',')

numbersSpoken = {}
previousNumbersSpoken = {}
turn =1
#dict where key = number and value = turns since last spoken

for i in range(len(_input)):
  numbersSpoken[int(_input[i])] = turn
  turn += 1

previousNumbersSpoken = dict(numbersSpoken)
toSpeak = None
lastSpoken = None

part1TurnCap = 2020
part2TurnCap = 30000000
part1 = False

while turn <= (part1TurnCap if part1 else part2TurnCap):
  
  if toSpeak == None:
    toSpeak = 0
    lastSpoken = toSpeak
    #print((turn, toSpeak))
    if toSpeak not in numbersSpoken:
      previousNumbersSpoken[toSpeak] = turn
      numbersSpoken[toSpeak] = turn
    else:
      previousNumbersSpoken[toSpeak] = numbersSpoken[toSpeak]
      numbersSpoken[toSpeak] = turn
    turn += 1
    continue
  
  turnsSinceLastSpoken = numbersSpoken[toSpeak] 
  turnsSincePreviouslyLaskSpoken = previousNumbersSpoken[toSpeak]

  toSpeak = turnsSinceLastSpoken - turnsSincePreviouslyLaskSpoken
  lastSpoken = toSpeak
  #print((turn, toSpeak))
  if toSpeak not in numbersSpoken:
    previousNumbersSpoken[toSpeak] = turn
    numbersSpoken[toSpeak] = turn
    toSpeak = None
  else:
    previousNumbersSpoken[toSpeak] = numbersSpoken[toSpeak]
    numbersSpoken[toSpeak] = turn
    
  turn += 1

print(lastSpoken)

