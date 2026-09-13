array = [2,3,3,4,2,8,9,3,7,2,2,2,2,2,2,2,22,2]
seen = {}
for i in array:
    if i in seen:
     seen[i] += 1
    else:
       seen[i] = 1
print(seen)