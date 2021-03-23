lim = int (input ("Enter pyramid limit:"))
for rowNum in range (1,lim+1) :
    row = ""
    for i in range (1,rowNum+1):
        row = row + str(rowNum)
    print (row)