number = [1, 2, 5, 6, 9]
target = 3

seen = {}

for i in number:

    required = target - i

    if required in seen:
        print(seen[required], i)

    seen[i] = i