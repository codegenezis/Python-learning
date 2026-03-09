# convert all the letters in the string "hello world" to their upper-case form
# check if it is a letter, before case conversion

string = "hello world"

result = [i.upper() for i in string if i.isalpha()]
print('result: {}'.format(result))