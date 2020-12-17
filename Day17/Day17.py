import sys
import math
import time
sys.path.append('./')
from adventInput import GetInput
import copy
import itertools
import collections

_input = GetInput(17)

#this code took 15 hours to run, dont run it.

class Cube:
  X = 0
  Y = 0
  Z = 0
  W = 0
  IsActive = False

  def __init__(self, x, y, z, w, isActive):
    self.X = x
    self.Y = y
    self.Z = z
    self.W = w
    self.IsActive = isActive

def AddMissing(cubes):
  newCubes = list(cubes)
  for cube in cubes:
    for x in [-1,0,1]:
      for y in [-1,0,1]:
        for z in [-1,0,1]:
          for w in [-1,0,1]:
            if x == 0 and y == 0 and z == 0 and w == 0:
              continue
            rPlusOffset = cube.X + x
            cPlusOffset = cube.Y + y
            zPlusOffset = cube.Z + z
            wPlusOffset = cube.W + w

            potentialCube = [c for c in newCubes if c.X == rPlusOffset and c.Y == cPlusOffset and c.Z == zPlusOffset and c.W == wPlusOffset]

            if len(potentialCube) == 0:
              c = Cube(rPlusOffset, cPlusOffset, zPlusOffset, wPlusOffset, False)
              newCubes.append(c)
  
  return newCubes

def checkAdjacent(cube, cubeMap):
  activeNeighbors = 0
  for x in [-1,0,1]:
    for y in [-1,0,1]:
      for z in [-1,0,1]:
        for w in [-1,0,1]:
          if x == 0 and y == 0 and z == 0 and w == 0:
            continue
          rPlusOffset = cube.X + x
          cPlusOffset = cube.Y + y
          zPlusOffset = cube.Z + z
          wPlusOffset = cube.W + w

          potentialCube = [c for c in cubeMap if c.X == rPlusOffset and c.Y == cPlusOffset and c.Z == zPlusOffset and c.W == wPlusOffset]

          if len(potentialCube) > 0:
            realCube = potentialCube[0]

            if realCube.IsActive:
              activeNeighbors += 1
            else:
              continue
  
  return activeNeighbors


def run(cubeMap, part1):
  i = 0
  startTime = time.time()
  while i < 6:
    iStart = time.time()
    changed = False
    cubeMap = AddMissing(cubeMap)
    modifiedCubeState = copy.deepcopy(cubeMap)

    for cubeIndex, cube in enumerate(modifiedCubeState):
      activeNeighbors = checkAdjacent(cube, cubeMap)

      if cube.IsActive and (activeNeighbors == 2 or activeNeighbors == 3):
        cube.IsActive = True
        
      elif not cube.IsActive and activeNeighbors == 3:
        cube.IsActive = True
      else:
        cube.IsActive = False

      #cubeState = newCubeState
    cubeMap = copy.deepcopy(modifiedCubeState)
    i += 1
    iEnd = time.time()
    print (f"i: {i} time: {iEnd - iStart}")
  
  endTime = time.time()
  print(f"Complete! time: {endTime-startTime}")
  return cubeMap




def initialize():
  cubes = []
  for rowIndex, row in enumerate(_input):
    for colIndex, col in enumerate(row):
      if col == '#':
        cube = Cube(colIndex, rowIndex, 0, 0, True)
      else:
        cube = Cube(colIndex, rowIndex, 0, 0, False)
      cubes.append(cube)
    
  
  return cubes
    
cubes = initialize()
#print (grid)

cubeMap = run(cubes, True)

ans = 0
for cube in cubeMap:
  if cube.IsActive:
    ans += 1

print (ans)

###
# i: 1 time: 5.859854221343994
# i: 2 time: 98.31523871421814
# i: 3 time: 650.8712351322174
# i: 4 time: 3093.2910392284393
# i: 5 time: 11431.747344493866
# i: 6 time: 39643.64871811867
# Complete! Poggers! time: 54923.737293720245
# ^^ in seconds. 15 hours total.
# 2160
#####