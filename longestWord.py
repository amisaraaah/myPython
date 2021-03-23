myList = []
num = int (input ("Enter number of Words :"))
print ("Enter words :")
for i in range (num) :
    item = input () 
    myList.append(item)
longestWord = ""
for word in myList:
    if len(word) > len(longestWord):
        longestWord = word
print("The length of the longest word is: %d"%len(longestWord))
