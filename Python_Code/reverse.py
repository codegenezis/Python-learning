# To reverse a number, you need to take the digits of the number and rearrange them in the opposite order.

num = int(input('Enter the number to reverse'))
temp_number = num
reverse = 0

while num > 0:
    reminder = num % 10
    # print('reminder', reminder)
    reverse = (reverse * 10) + reminder
    # print('reverse', reverse)
    num = num // 10
    # print('num', num)

print ("the value entered is {} and the reverse is {}".format(temp_number, reverse))