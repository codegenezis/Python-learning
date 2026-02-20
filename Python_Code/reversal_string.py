def reversal(data):
    print(data)
    # data[::-1] --> starts from the end and streps backward to the start
    reversed_value = data[::-1]

    try:
        return int(reversed_value)
    except ValueError:
        pass   # pass if the string is not Integer

    try:
        return float(reversed_value)
    except ValueError:
        pass

    # Here if the string is not integer or float directly retured as string
    return reversed_value
    


user_value = input('Type in the string for reversal:')
print("user Entered value is:", reversal(user_value))