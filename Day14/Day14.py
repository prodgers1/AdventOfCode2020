import sys
import math
import time
sys.path.append('./')
from adventInput import GetInput
import copy
import itertools
import collections

_input = GetInput(14)


def maskValue(mask, value):
  mask = list(mask)
  value = list(value)

  maskedValue = value
  i = len(mask)-1

  while i >= 0:
    currentMaskValue = mask[i]
    currentValue = value[i]
    
    if currentMaskValue == 'X' or currentMaskValue == currentValue:
      i -= 1
      continue

    maskedValue[i] = currentMaskValue
    i -= 1

  return ''.join(maskedValue)

def maskAddress(mask, address):
  mask = list(mask)
  address = list(address)

  maskedAddress = address
  i = len(mask)-1

  while i >= 0:
    currentMaskValue = mask[i]
    currentValue = address[i]
    
    if currentMaskValue == "0":
      i -= 1
      continue

    maskedAddress[i] = currentMaskValue
    i -= 1

  return ''.join(maskedAddress)

def replaceX(address, currentBinaryXValue):
  address = list(address)

  indicies = [i for i, x in enumerate(address) if x == 'X']
  j = 0
  for index in indicies:
    address[index] = currentBinaryXValue[j]
    j += 1
  
  return ''.join(address)


def part2():
  mask = ""
  memory = {}
  for line in _input:
    splitLine = line.split()
    if splitLine[0] == 'mask':
      mask = splitLine[2]
    
    if splitLine[0].startswith('mem'):
      memoryAddress = int(splitLine[0].split('[')[1].replace(']', ''))
      value = int(splitLine[2])
      binaryAddressValue = "{0:b}".format(memoryAddress).rjust(len(mask), '0')
      assert len(binaryAddressValue) == len(mask)

      maskedMemoryAddress = maskAddress(mask, binaryAddressValue)
      exponent = maskedMemoryAddress.count('X')
      combinations = 2**exponent

      for i in range(combinations):
        #convert current index to binary, then right justify with 0's to fill in the gap
        #so that i have the correct number of binary slots filled, so i can replace
        # them using the index of the X's in replaceX
        binaryPad = "{0:b}".format(i).rjust(exponent, '0')
        newAddress = replaceX(maskedMemoryAddress, binaryPad)
        memory[int(newAddress, 2)] = value



  ans = 0
  for key, value in memory.items():
    ans += value
  print (ans)

def part1():
  mask = ""
  memory = {}
  for line in _input:
    splitLine = line.split()
    if splitLine[0] == 'mask':
      mask = splitLine[2]
    
    if splitLine[0].startswith('mem'):
      memoryAddress = int(splitLine[0].split('[')[1].replace(']', ''))
      value = int(splitLine[2])
      #convert to binary number, then fill in with 0's (left of the value) for missing indexes (so the lengths of the mask and value match)
      binaryValue = "{0:b}".format(value).rjust(len(mask), '0')
      assert len(binaryValue) == len(mask)
      maskedValue = maskValue(mask, binaryValue)


      memory[memoryAddress] = maskedValue


  ans = 0
  for key, value in memory.items():
    ans += int(value,2)
  print (ans)


part1()
part2()