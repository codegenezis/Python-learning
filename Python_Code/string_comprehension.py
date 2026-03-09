# Python program to drop all digits from a string.

mystr = 'He12llo, Py00th55on!'
digit=[str(i) for i in range(10)] 
char=[]

for x in mystr:
    if x not in digit:
        char.append(x)  #appending the char to char list

newstr = "".join(char) #join all the char in the list
print("mystr:{}, digit:{}, newstr:{}".format(mystr, digit, newstr))