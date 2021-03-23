# Write a Python program which gets multiple words as input and calculate the number
#  of letters present in each one of them.For example, if the following input is
#  given to the program:VIT Then, the output should be:No. of LETTERS 3

word_list = []
length_list = []
input_word = ' '
print('Enter the words below: ')
while(input_word != ''):
    input_word = input()
    word_list.append(input_word)

word_list.pop()
print('The entered words are:' +str(word_list))

for i in range(len(word_list)):
    length_list.append(len(word_list[i]))

for j in range(len(word_list)):
    print('The no. of LETTERS in '+str(word_list[j])+' is '+str(length_list[j]))