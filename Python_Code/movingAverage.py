def movingAverage(data, window_size):
    if window_size <= 0:
        raise ValueError("Window size must be greater than 0.")
    
    moving_averages = []
    print('1 ==>', range(len(data) - window_size + 1))
    for i in range(len(data) - window_size + 1):
        window = data[i:i + window_size]
        print('2 ==>', window)
        average = sum(window) / window_size
        print('3 ==>', average)
        moving_averages.append(average)
    
    return moving_averages

prices = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# movingAverage(prices, window_size=3)
print(movingAverage(prices, window_size=3))