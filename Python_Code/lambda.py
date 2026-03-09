# lambda is a keyword used to create anonymous functions

# double each element in the given list:

original_list = [1, 2, 3, 4, 5]

doubled_list = [(lambda i: i ** 2)(i) for i in original_list]
print(doubled_list)

# 2. list of tuples (like employee data) and want to sort by the second element:

data = [("Kiran", 30), ("Amit", 25), ("Ananya", 28)]
data.sort(key = lambda x: x[1])
print(data)

# 3. grab only even numbers from a list:

numbers = [1, 2, 3, 4, 5, 6]
# result = list(filter(lambda x: x%2 == 0, numbers))
result = filter(lambda x: x%2 == 0, numbers)
print(result)

for i in result:
    print(i)

# The filter() function doesn't actually create a new list. Instead, it creates a Filter Object (an iterator).
# With list(): You have the actual even numbers stored in memory.

# Nested Loops in Python List Comprehension

list1=[1,2,3]
list2=[4,5,6]

result = [(i,j) for i in list1 for j in list2]
print("Result is {}:".format(result))


# generate a list of even numbers from 1 to 20 −

list = [ i for i in range(1,21) if i %2 == 0]
print('list of even no: {}'.format(list))

# we want to separate each letter in a string and put all non-vowel letters in a list object

list = [i for i in 'TutorialsPoint' if i not in 'aeiou']
print("non vowels: {}". format(list))

# Sorting List:
# list_name.sort(key=None, reverse=False)

numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
# Sorting in descending order
sorted_numbers_desc = sorted(numbers, reverse=True)
print(sorted_numbers_desc) 

# other option:
list1 = ['Physics', 'biology', 'Biomechanics', 'psychology']
list1.sort(key=str.lower)