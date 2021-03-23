d = 1
#start x = cos(angle) z = tan(angle) 
x = 1
i = 10
z = 1.193359375
y = -0.0016593750000000185
if y > 0 :
    d = -1
print("i = ",i)
print ("d =",d)
nextZ = z - (d*2**(-i))
print ("z = ",nextZ)
sinz = y + (d*x*2**(-i))
print ("y = ",sinz)