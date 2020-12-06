import sys
import math
import time
sys.path.append('./')
from adventInput import GetInput

_input = GetInput(6)

indicies = [i for i,x in enumerate(_input) if x == ""]
indicies.append(len(_input))
i = 0

part1YesAnswers = 0
part2YesAnswers = 0

for index in indicies:
  group = _input[i:index]
  part1 = list()
  part2 = list()
  for member in group:
    memberQuestionAnswered = set()
    for question in member:
      memberQuestionAnswered.add(question)
      if question not in part1:
        part1.append(question)
        part1YesAnswers += 1
    part2.append(memberQuestionAnswered)

  result = part2[0]
  for l in part2[1:]:
    result = result.intersection(l)
  part2YesAnswers += len(result)
  i = index + 1

print(part1YesAnswers)
print(part2YesAnswers)