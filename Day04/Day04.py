import sys
import math
sys.path.append('./')
from adventInput import GetInput

_input = GetInput(4)

indicies = [i for i,x in enumerate(_input) if x == ""]
indicies.append(len(_input))
requiredValues = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]
i = 0
passports = []
for indexOfNextPassport in indicies:
  potentialPassportLines = _input[i:indexOfNextPassport]
  newPassport = {}
  for line in potentialPassportLines:
    spaceSplit = line.split(' ')
    for keyValue in spaceSplit:
      key = keyValue.split(':')[0]
      value = keyValue.split(':')[1]
      newPassport[key]=value
  passports.append(newPassport)
  i = indexOfNextPassport + 1

eyeColors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
validPassports = 0
for passport in passports:
  valid = True
  allKeys = passport.keys()
  keysLength = len(allKeys)
  for key in requiredValues:
    if key not in allKeys and key != 'cid':
      valid = False
      break
    
    if key == "cid":
      continue
    value = passport[key]

    if key == "byr":
      value = int(value)
      valid = len(str(value)) == 4 and (value >= 1920 and value <= 2002)
    elif key == "iyr":
      value = int(value)
      valid = len(str(value)) == 4 and (value >= 2010 and value <= 2020)
    elif key == "eyr":
      value = int(value)
      valid = len(str(value)) == 4 and (value >= 2020 and value <= 2030)
    elif key == "hgt":
      if "cm" in value:
        cmValue = int(value.split('cm')[0])
        valid = cmValue >= 150 and cmValue <= 193
      elif "in" in value:
        inValue = int(value.split('in')[0])
        valid = inValue >= 59 and inValue <= 76
      else:
        valid = False
    elif key == "hcl":
      valueLength = len(value)
      valid = (value[0] == '#' and len(value[1:valueLength]) == 6)
      validInts = ["0","1","2","3","4","5","6","7","8","9"]
      validChars = ["a", "b", "c", "d", "e", "f"]
      if not valid:
        break
      for char in value[1:valueLength]:
        valid = (char in validInts or char in validChars)
        if not valid:
          break
      
    elif key == "ecl":
      valid = value in eyeColors
    elif key == "pid":
      valid = len(value) == 9
      for char in value:
        if not char.isdigit():
          valid = False
          break
    
    if not valid:
      break

  if valid:
    validPassports+=1
      
print(validPassports)