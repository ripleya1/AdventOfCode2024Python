import re

sum = 0

def isValid(expression):
    if(re.search("^(m(u(l(\(([0-9]+(,([0-9]+(\)?)?)?)?)?)?)?)?)$", expression) != None):
        return True
    return False

def isCompletelyValid(expression):
    if(re.search("(mul)\([0-9]+,[0-9]+\)", expression) != None):
        print(expression)
        return True
    return False

def getNumsFromValidExpression(expression):
    temp = expression.split("(")[1].split(",")
    return [int(temp[0]), int(temp[1].split(")")[0])]

with open("day3input.txt") as f:
    for line in f:
        currExpression = ""
        for char in line:
            if(len(currExpression) == 0 and char != 'm'):
                continue
            currExpression += char
            if(not isValid(currExpression)):
                currExpression = ""
            elif(isCompletelyValid(currExpression)):
                nums = getNumsFromValidExpression(currExpression)
                sum += (nums[0] * nums[1])
                currExpression = ""

print(sum)