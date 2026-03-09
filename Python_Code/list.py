lst = [25, 12, 10, -21, 10, 100]

# For Loop
#end = '' make the output to display in one line
for i in lst:
    print(i, end = '')


# while loop:
index = 0;
while index < len(lst):
    print(lst[index])

    index = index + 1


# loop through the list with index:

index = range(len(lst))
for i in index:
    print('lst[{}]:'.format(i), lst[i])

# List Comprehension:

list1 = [1,2,3,4,5]
squared_value = [i ** 2 for i in list1]
print(squared_value)

#The enumerate() function in Python is used to iterate over an iterable object while also providing the index of each element.

fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print('fruit is {}'.format(fruit), index)