import sys
import math
sys.path.append('./')
from adventInput import GetInput

_input = GetInput(1)

for x in _input:
  for y in _input:
    for z in _input:
      x = int(x)
      z = int(z)
      y = int(y)
      if x != y and x != z and y != z:
        if x + y + z == 2020:
          print(x*y*z)
          break