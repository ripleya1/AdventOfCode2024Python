IdList1 = []
IdList2 = []
Id1 = 0
Id2 = 0
with open("day1input.txt") as f:
    for line in f:
        Id1 = int(line.split("   ")[0])
        Id2 = int(line.split("   ")[1])
        i = 0

        while i < len(IdList1) and Id1 > IdList1[i]:
            i += 1
        IdList1.insert(i, Id1)

        i = 0
        while i < len(IdList2) and Id2 > IdList2[i]:
            i += 1
        IdList2.insert(i, Id2)

# print(IdList1)
# print(IdList2)

sum = 0
for i in range(len(IdList1)):
    sum += abs(IdList1[i] - IdList2[i])

print(sum)