myList = []
num = int (input ("Enter number to add to a list :"))
print ("Enter few things :")
for i in range (num) :
    item = input () 
    myList.append(item)
print ("copying List . . .")
copyList = myList.copy()
print ("the copy list is :" + str(copyList))
