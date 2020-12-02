import sys
import math
sys.path.append('./')
from adventInput import GetInput

_input = GetInput(2)
valid = list()

for rule in _input:
  ruleSplit = rule.split(' ')
  nums = ruleSplit[0].split('-')
  lowBound = int(nums[0])
  highBound = int(nums[1])
  neccessaryChar = ruleSplit[1].split(":")[0]

  password = ruleSplit[2]

  charCount = password.count(neccessaryChar)

  if charCount < lowBound or charCount > highBound:
    continue

  valid.append(rule)

print(len(valid))
valid.clear()

for rule in _input:
  ruleSplit = rule.split(' ')
  nums = ruleSplit[0].split('-')
  firstPosition = int(nums[0]) - 1
  lastPosition = int(nums[1]) - 1

  neccessaryChar = ruleSplit[1].split(":")[0]

  password = ruleSplit[2]

  if ((password[firstPosition] == neccessaryChar or password[lastPosition] == neccessaryChar) and
    not(password[firstPosition] == neccessaryChar and password[lastPosition] == neccessaryChar)):
    valid.append(rule)

print(len(valid))