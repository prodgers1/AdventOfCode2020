import sys
import math
import time
sys.path.append('./')
from adventInput import GetInput
import copy
import itertools
import collections

_input = GetInput(13)


def part1(): 
  buses = []
  earliestDepart = int(_input[0])
  splitInput = _input[1].split(',')
  for line in splitInput:
    if line != 'x':
      buses.append(int(line))

  busArrivals = {}

  for bus in buses:
    numberOfStops = round(earliestDepart / bus)
    busArrivals[bus] = numberOfStops * bus

  sortedDict = {k: v for k, v in sorted(busArrivals.items(), key=lambda item: item[1])}

  for busArrival in sortedDict.items():
    if busArrival[1] < earliestDepart:
      continue
    diff = earliestDepart - busArrival[1]
    print(abs(busArrival[0] * diff))
    break

#literally copied and pasted from the interwebs because wtf
from functools import reduce
def chinese_remainder(n, a):
    _sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        _sum += a_i * mul_inv(p, n_i) * p
    return _sum % prod
 
def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

def part2():
  buses = {}
  
  n = []
  a = []
  
  splitInput = _input[1].split(',')
  for i in range(len(splitInput)):
    if splitInput[i] == 'x':
      continue
    n.append(int(splitInput[i]))
    a.append(i)
    buses[i] = int(splitInput[i])
  #print(buses)

  for i in range(len(a)):
    a[i] = n[i] - a[i]

  print(chinese_remainder(n,a))

  # timestamp = 100000000000000
  # while True:
  #   start = {}
  #   for bus in buses.items():
  #     if bus[1] == 'x':
  #       continue
  #     busId = int(bus[1])
  #     stops = round(timestamp / busId)
  #     willStartAt = stops * busId
  #     start[busId] = willStartAt

  #   inRange = True
  #   for busNum, leave in start.items():
  #     for bus in buses.items():
  #       if bus[1] == busNum:
  #         busToCheck = bus
  #         break
  #     offset = busToCheck[0]
  #     if leave - timestamp == offset:
  #       continue
  #     inRange = False
  #     break
  #   if inRange:
  #     print(timestamp)
  #     break
  #   timestamp += 1


part1()
part2()
