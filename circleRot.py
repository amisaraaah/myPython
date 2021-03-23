e = [45, 26.56, 14, 7.12, 3.57, 1.79, 0.895, 0.447, 0.224, 0.112, 0.056]
d = 1

i = 9
z = -0.2
x = 0.25673989801273256
y = 0.9664780145324531
if z <0 :
    d = -1
print("i = ",i)
nextZ = z - (d*e[i])
print (nextZ)
cosz = x - (d*y*2**(-i))
print (cosz)
sinz = y + (d*x*2**(-i))
print (sinz)