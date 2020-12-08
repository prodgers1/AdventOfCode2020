import sys
import math
import time
sys.path.append('./')
from adventInput import GetInput
from collections import defaultdict
import copy

_input = GetInput(8)

def part1():
  accumulator = 0
  ip = 0
  pc = 0
  SEEN = {}
  while True:
    commandLine = _input[ip]
    command, value = commandLine.split()
    pc += 1
    
    if ip in SEEN and commandLine in SEEN[ip]:
      break

    SEEN[ip] = commandLine
    v = int(value)
    
    if command == 'nop':
      ip += 1
    elif command == 'acc':
      accumulator += v
      ip += 1
    elif command == 'jmp':
      ip = (ip + v)
    else:
      ip += 1
  return accumulator

def tryNewMutation(resetInput): 
  iterations = 0
  accumulator = 0
  ip = 0
  pc = 0
  SEEN = {}
  totalInstructionCount = len(resetInput)

  while True:
    iterations += 1
    if ip >= totalInstructionCount:
      return True, accumulator

    if ip in SEEN:
      return False, accumulator

    commandLine = resetInput[ip]
    command, value = commandLine.split()
    pc += 1
    v = int(value)
    SEEN[ip] = commandLine

    if command == 'nop':
      ip += 1
    elif command == 'acc':
      accumulator += v
      ip += 1
    elif command == 'jmp':
      ip = (ip + v)
    else:
      ip += 1

def resetTheInput(originalInput, index):
  resetInput = copy.deepcopy(_input)
    
  if resetInput[index].split()[0] == 'jmp':
    line = resetInput[index]
    resetInput[index] = line.replace('jmp', 'nop')
    
  elif resetInput[index].split()[0] == 'nop':
    line = resetInput[index]
    resetInput[index] = line.replace('nop', 'jmp')
  
  # print(f"----Trying index:{index} {resetInput[index]} -------")
  return resetInput

def part2():
  indicies = [i for i,x in enumerate(_input) if x.split()[0] == 'jmp' or x.split()[0] == 'nop']
  for index in indicies:
    
    resetInput = resetTheInput(_input, index)
    success, accumulator = tryNewMutation(resetInput)
    if success:
      return accumulator
      
print(part1())
print(part2())