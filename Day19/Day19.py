import sys
import math
import time
sys.path.append('./')
from adventInput import GetInput
import copy
import itertools
import collections

_input = GetInput(19)

rules = {}

indexOfRuleEnd = _input.index('')

rulesInput = _input[:indexOfRuleEnd]
testsInput = _input[indexOfRuleEnd+1:]

for rule in rulesInput:
  splitRule = rule.split()
  ruleId = splitRule[0].replace(':', '')
  rules[ruleId] = list()
  currentRuleList = list()
  for index in range(1, len(splitRule)):
    if splitRule[index] == '|':
      rules[ruleId].append(currentRuleList)
      currentRuleList = list()
    elif splitRule[index].startswith('"'):
      rules[ruleId] = splitRule[index].replace('"', "")
    else:
      currentRuleList.append(splitRule[index])
  if len(currentRuleList) > 0:
    rules[ruleId].append(currentRuleList)

class Parser:

  def __init__(self, token, rules):
    self.Token = token
    self.Rules = rules
    self.Index = 0
    self.StartingIndex = 0
    self.TokensChecked = []

  def IsValidConstant(self, constant):
    valid = self.GetToken(constant)
    return valid

  def ParseGrammar(self, rule, token = ''):
    result = None
    if rule in self.Rules:
      subRules = self.Rules[rule]
      for i, subRule in enumerate(subRules):

        if type(subRule) != type(list()) and subRule not in self.Rules:
          token = self.GetToken()
          if token == subRule:
            result = True
          else:
            #self.UngetToken()
            result = False
          break

        tokensGot = list()
        if result:
          break
        for subSubRule in subRule:
          #get token to check if it works in this rule, if it doesnt, unget it. if a subsequent rule following this one fails,
          #unget both of them
          # token = self.GetToken()
          # tokensGot.append(token)
          result = self.ParseGrammar(subSubRule)
          if not result:
            self.UngetToken()
            result = False
            break # this subrule doesnt work, but potentially teh following will
    else:
      # im a constant
      result = self.IsValidConstant(rule)

      if not result:
        return False

    return result

  def Parse(self):
    zeroRule = self.Rules['0']

    for rule in zeroRule[0]:
      result = self.ParseGrammar(rule)
      if not result:
        return False
      self.StartingIndex = self.Index

    if self.StartingIndex < len(self.Token):
      return False
    
    return True

#the get and unget are incorrect. need to somehow calculate how many rules i have, and unget that amount
  def GetToken(self):
    if self.Index >= len(self.Token):
      assert False
    char = self.Token[self.Index]
    self.Index += 1
    return char
    # if char == constant:
    #   self.Index += 1
    #   self.TokensChecked.append(char)
    #   return True
    # return False

  def UngetToken(self):
    self.Index -= 1


ans = 0

for test in testsInput:
  parser = Parser(test, rules)
  try:
    result = parser.Parse()
  except:
    result = False
    print(f"{test} too short")
  #print(result)
  if result:
    ans += 1

print(ans)
