print ("\nTo convert enter (1) for Celsius to Fahrenheit (2) for Fahrenheit to Celsius")
choice = int (input("Enter Your Choice: "))
if choice==1 or choice==2:
    temp = float (input ("Enter temperature: "))
    if choice == 1:
        #convert C to F
        tempConv = (temp * 1.8) + 32 
        print("%.2f°C is %.2f in Fahrenheit"%(temp,tempConv))
    else:
        #convert F to C
        tempConv = (temp - 32) / 1.8
        print("%.2f°F is %.2f in Celsius"%(temp,tempConv))
else:
    print("Invalid Choice")