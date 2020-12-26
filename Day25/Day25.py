import sys
import math
import time
sys.path.append('./')
from adventInput import GetInput
import copy
import itertools
import collections

_input = GetInput(25)

def transform(subject, loopSize):
  #raise subject to loopsize exponent, then mod that answer by the third parameter
  return pow(subject, loopSize, 20201227)

def findLoopSize(publicKey):
  potentialLoopSize = 1
  while transform(7, potentialLoopSize) != publicKey:
    potentialLoopSize += 1
  
  return potentialLoopSize


cardPublicKey = int(_input[0])
doorPublicKey = int(_input[1])

cardLoopSize = findLoopSize(cardPublicKey)
doorLoopSize = findLoopSize(doorPublicKey)

encryptionKey = transform(cardPublicKey, doorLoopSize)
print(encryptionKey)