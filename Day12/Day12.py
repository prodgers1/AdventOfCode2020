import sys
import math
import time
sys.path.append('./')
from adventInput import GetInput
import copy
import itertools
import collections

_input = GetInput(12)

directions = []

for line in _input:
  direction = line[0]
  units = int(line[1:])
  directions.append({"direction": direction, "units": units})

nextDirections = {}
nextDirections["N"] = ["E", "S", 'W']
nextDirections["E"] = ["S", "W", "N"]
nextDirections["S"] = ['W', 'N', "E"]
nextDirections["W"] = ["N", "E", "S"]

def turn(currentDirection, directionToTurn, degrees):
  path = nextDirections[currentDirection]

  turns = degrees // 90
  
  for i in range(turns):
    if directionToTurn == "R":
      currentDirection = path[i]
    elif directionToTurn == "L":
      copyList = list(path)
      copyList.reverse()
      currentDirection = copyList[i]

  return currentDirection

def move(direction):
  global x,y, currentDirection
  d = direction["direction"]
  units = direction["units"]

  if d == "N":
    y -= units
  
  if d == "E":
    x += units

  if d == "S":
    y += units

  if d == "W":
    x -= units
  
  if d == "L": 
    currentDirection = turn(currentDirection, "L", units)
    
  if d == "R":
    currentDirection = turn(currentDirection, "R", units)

  if d == "F":
    if currentDirection == "N":
      y -= units
    
    if currentDirection == "E":
      x += units
    
    if currentDirection == "S":
      y += units

    if currentDirection == "W":
      x -= units

def turnWaypoint(directionToTurn, waypointPosition, degrees):
  turns = degrees // 90
  for i in range(turns):
    waypointX = waypointPosition[0]
    waypointY = waypointPosition[1]
    if directionToTurn == "R":
      # x position = -y position
      # y position = x position
      waypointPosition = (-waypointY, waypointX)

    elif directionToTurn == 'L':
      # x position = y position
      # y position = -x position
      waypointPosition = (waypointY, -waypointX) 
  
  return waypointPosition

def moveWaypoint(direction):
  global x,y, waypointPosition 
  d = direction["direction"]
  units = direction["units"]

  if d == "N":
    waypointPosition = (waypointPosition[0], waypointPosition[1] - units )
  
  if d == "E":
    waypointPosition = (waypointPosition[0] + units , waypointPosition[1])

  if d == "S":
    waypointPosition = (waypointPosition[0], waypointPosition[1] + units)

  if d == "W":
    waypointPosition = (waypointPosition[0] - units , waypointPosition[1])
  
  if d == "L": 
    waypointPosition = turnWaypoint("L", waypointPosition, units)
    
  if d == "R":
    waypointPosition = turnWaypoint("R", waypointPosition, units)

  if d == "F":
   #teleport to waypoint n times
   x = x + ((waypointPosition[0]) * units)
   y = y + ((waypointPosition[1]) * units)

x = 0
y = 0
currentDirection = "E"

for direction in directions:
  move(direction)

distance = abs(x) + abs(y)
print(distance)

x = 0
y = 0
waypointPosition = (10, -1)
for direction in directions:
  moveWaypoint(direction)

distance = abs(x) + abs(y)
print(distance)