#longest increasing streak
temps = [23, 25, 27, 26, 28, 30, 32, 31, 35]

current = 1
largest = 1

for i in range(1, len(temps)):

    if temps[i] > temps[i - 1]:
        current = current + 1

        if current > largest:
            largest = current

    else:
        current = 1

print(largest)

    

    