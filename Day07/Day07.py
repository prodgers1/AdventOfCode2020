import sys
import math
import time
sys.path.append('./')
from adventInput import GetInput

_input = GetInput(7)

class Bag:
    
  def __init__(self):
    self.Contains = []
    self.Color = ""
    self.Adj = ""
    self.Count = 0
    self.ContainsGold = False

  def CreateRules(self, line):
    containSplit = line.split('contain')
    bagDefinition = containSplit[0].split(' ')
    adj = bagDefinition[0]
    color = bagDefinition[1]
    
    self.Adj = adj
    self.Color = color

    containsList = containSplit[1].strip().split(' ')
    indicies = [i for i,x in enumerate(containsList) if x.isdigit()]
    
    for index, bagIndex in enumerate(indicies):
      bagDescription = containsList[index * 4:bagIndex+3]
      bag = Bag()
      bag.Count = int(bagDescription[0])
      bag.Adj = bagDescription[1]
      bag.Color = bagDescription[2]
      self.Contains.append(bag)
    
  def FindGoldBag(self, bags):
    for childBag in self.Contains:

      if self.ContainsGold or childBag.ContainsGold or childBag.IsGoldBag():
        return True
      
      matchingBag = [b for b in bags if b.Color == childBag.Color and b.Adj == childBag.Adj][0]
   
      found = matchingBag.FindGoldBag(bags)
      childBag.ContainsGold = found
      self.ContainsGold = found

      if found:
        return True


    return False
  
  def IsGoldBag(self):
    return self.Color == "gold" and self.Adj == "shiny"

  def FindHowManyBags(self, bags):
    count = 0
    for childBag in self.Contains:
      
      matchingBag = [b for b in bags if b.Color == childBag.Color and b.Adj == childBag.Adj][0]

      if len(matchingBag.Contains) == 0:
        count += childBag.Count
        continue

      totalBagsBeneath = matchingBag.FindHowManyBags(bags)
      sumBeneath = totalBagsBeneath * childBag.Count

      count += (sumBeneath +  childBag.Count)

    return count
  

bags = list()


for line in _input:
  bag = Bag()
  bag.CreateRules(line)
  bags.append(bag)

startTime = time.time()
count = 0
for bag in bags:
  containsShiny = bag.FindGoldBag(bags)
  if containsShiny:
    count += 1

endTime = time.time()
print(endTime - startTime)
print(count)

shinyGoldBag = [b for b in bags if b.Color == "gold" and b.Adj == "shiny"][0]

startTime = time.time()
count = shinyGoldBag.FindHowManyBags(bags)
endTime = time.time()
print(endTime - startTime)
print(count)