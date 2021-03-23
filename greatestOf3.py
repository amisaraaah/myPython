num1 = int (input ("Enter number 1:") )
num2 = int (input ("Enter number 2:") )
num3 = int (input ("Enter number 3:") )
if (num1 > num2) :
    if (num1 > num3) :
        ans = num1
    else :
        ans = num3
else :
    if (num2 > num3) :
        ans = num2
    else :
        ans = num3
print ("Greatest number is ",ans)