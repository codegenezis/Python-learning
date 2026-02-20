def fibonacci(n):

    if (n <= 0):
        print("Please end the positive integer")
        return
    
    # val1=0
    # val2=1

    val1, val2 = 0,1

    print(val1, val2, end =' ' )

    for i in range(2, n):
        val3 = val1 + val2
        # val1 = val2
        # val2=val3

        val1, val2 = val2, val1+val2  #tuple unpacking  -> calculates entirely before assigning to left side

        print(val3, end=' ')

end_value = int(input("Enter the value:"))
fibonacci(end_value)