import math
C = 50
H = 30
dList = input ("Enter D values: ").split(",")
DList = []
for d in dList:
    DList.append(int(d))
resultList = []
for D in DList:
    result = math.sqrt((2*C*D)/H)
    resultList.append(round(result))
print(",".join(map(str,resultList)))