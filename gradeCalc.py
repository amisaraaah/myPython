num = int (input ("Enter number  of students:"))
for i in range (num) :
    print ("Student (%d/%d)"%(i+1,num))
    att = int (input ("Enter Attendance:"))
    if att >= 75:
        mark = int (input ("Enter Mark: "))
        if (mark < 50) :
            print ("Your Grade is F")
        elif (mark >= 50 and mark < 60) :
            print ("Your Grade is E")
        elif (mark >= 60 and mark < 70) :
            print ("Your Grade is D")
        elif (mark >= 70 and mark < 80) :
            print ("Your Grade is C")
        elif (mark >= 80 and mark < 90) :
            print ("Your Grade is B")
        elif (mark >= 90 and mark < 95) :
            print ("Your Grade is A")
        elif (mark >= 95 and mark < 100) :
            print ("Your Grade is S")
    else :
        print ("Your Grade is F")
    