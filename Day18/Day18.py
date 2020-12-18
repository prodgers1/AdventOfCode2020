import sys
import math
import time
sys.path.append('./')
from adventInput import GetInput
import copy
import itertools
import collections

_input = GetInput(18)
part1 = False

def Evaluate(ex, operator = ''):
  splitExpression = ex.split()

  #take first operator from L -> R because math
  if len(operator) == 0:
    operatorIndex = [i for i, v in enumerate(splitExpression) if v == "*" or v == "+"][0]
  else:
    operatorIndex = [i for i, v in enumerate(splitExpression) if v == operator][0]

  lhs, op, rhs = splitExpression[operatorIndex-1], splitExpression[operatorIndex], splitExpression[operatorIndex+1]

  lhs = int(lhs)
  rhs = int(rhs)
  if op == '+':
    ans = lhs + rhs
  elif op == '*':
    ans = lhs * rhs
  
  splitExpression[operatorIndex-1] = ''
  splitExpression[operatorIndex] = ''
  splitExpression[operatorIndex + 1] = str(ans)       

  ex = ' '.join(splitExpression) 
  return ex, ans

def EvaluateExpression(expression):
  ans = 0
  while "*" in expression or "+" in expression:
    if '(' in expression:
      startParenthesisIndex = expression.rfind('(')
      endParenthesisIndex = expression.find(')', startParenthesisIndex)
      subExpression = expression[startParenthesisIndex+1:endParenthesisIndex]

      ans = EvaluateExpression(subExpression)
      expression = expression[:startParenthesisIndex] + str(ans) + expression[endParenthesisIndex+1:]
      
    elif part1:
      expression, ans = Evaluate(expression)
      
    elif not part1:
      if '+' in expression:
        expression, ans = Evaluate(expression, '+')
      else:
        expression, ans = Evaluate(expression, '*')      

  return ans

ans = 0
for expression in _input:
  ans += EvaluateExpression(expression)
  #print(EvaluateExpression(expression))

print (ans)