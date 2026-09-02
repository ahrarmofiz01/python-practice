# 1. Rename the variable to avoid using the built-in 'list' keyword
numbers = [2, 3, 10, 15, 8]
target = 5
freq = {}

for i in numbers:
    r = target - i
    if r in freq:
        print([r, i])
    
    # 2. Add the current number to the dictionary so future iterations can find it
    freq[i]=True
