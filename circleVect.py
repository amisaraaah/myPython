e = [45, 26.56, 14, 7.12, 3.57, 1.79, 0.895, 0.447, 0.224, 0.112, 0.056]
d = -1
i = 10
z = 50.114000000000004
x = 2.5618328378306865
y = -0.00327872053739154
if y > 0 :
    d = -1
else:
    d = 1
print("i = ",i)
print("d = ",d)
nextZ = z - (d*e[i])
print ("z = ",nextZ)
cosz = x - (d*y*2**(-i))
print ("x = ",cosz)
sinz = y + (d*x*2**(-i))
print ("y = ",sinz)
