lim = int (input ("Enter fibonacci limit:"))
a,b = 0,1
while b < lim :
    print(b,end = ' ')
    a, b = b, a+b
