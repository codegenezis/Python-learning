def reversal(n, data):
    '''
    this is the reversal function with user option to choose
    different slicing method using
    1. slicing method
    2. Functional method using reversed() 
    3. manual method
    '''
    match n:
        case 1:
            # slicing method
            reversed_str = data[::-1]
            return reversed_str
        case 2:
            # Functional method (reversed())
            reversed_str = "" .join(reversed(data))
            return reversed_str
        case 3:
            # manual method
            char = ''
            reversed_str=''
            for i in data:
                reversed_str = char + i
            return reversed_str

# To see the documentation
help(reversal)

text = "kiran"
option = int(input("Enter the value:"))
print(reversal(1, text))