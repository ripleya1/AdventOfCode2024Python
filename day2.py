numSafeReports = 0

with open("day2input.txt") as f:
    for line in f:
        decreasing = True
        prevNum = -1
        numSafeReports += 1
        i = 0
        for num in line.split(" "):
            num = int(num)
            if(prevNum >= 0):
                if(i == 1 and (prevNum - num) > 0):
                    decreasing = False
                if(((decreasing) and ((prevNum - num) >= 0)) or ((not decreasing) and ((prevNum - num) <= 0))):
                    numSafeReports -= 1
                    break
                if(abs(prevNum - num) > 3):
                    numSafeReports -= 1
                    break
            prevNum = num
            i += 1

print(numSafeReports)