import re

sum = 0

def isValidDoOrDont(expression):
    if(re.search("^d(?:o(?:n(?:'?t?)?)?)?\(?\)?$", expression)):
        return True
    return False

def isCompletelyValidDoOrDont(expression):
    if(re.search("do(n't)?\(\)", expression)):
        return True
    return False

def isValidMul(expression):
    if(re.search("^(m(u(l(\(([0-9]+(,([0-9]+(\)?)?)?)?)?)?)?)?)$", expression)):
        return True
    return False

def isCompletelyValidMul(expression):
    if(re.search("(mul)\([0-9]+,[0-9]+\)", expression)):
        return True
    return False

def getNumsFromValidExpression(expression):
    temp = expression.split("(")[1].split(",")
    return [int(temp[0]), int(temp[1].split(")")[0])]

with open("day3input.txt") as f:
    enabled = True
    for line in f:
        currExpression = ""
        mul = True
                
        for char in line:
            if(len(currExpression) == 0):
                if(char != 'm' and char != 'd'):
                    continue
                elif(char == 'm'):
                    mul = True
                elif(char == 'd'):
                    mul = False

            currExpression += char
            
            if(not mul and not isValidDoOrDont(currExpression)):
                currExpression = ""
            elif(not mul and isCompletelyValidDoOrDont(currExpression)):
                if(currExpression == "do()"):
                    enabled = True
                elif(currExpression == "don't()"):
                    enabled = False
                currExpression = ""
            
            if((mul and not isValidMul(currExpression)) or (mul and not enabled)):
                currExpression = ""
            elif(mul and enabled and isCompletelyValidMul(currExpression)):
                nums = getNumsFromValidExpression(currExpression)
                sum += (nums[0] * nums[1])
                currExpression = ""

print(sum)