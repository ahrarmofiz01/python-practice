array=[8,0,2,9,29,0,0,2,1.23,4]
seen={}
for i in array:
    if i in  seen:
        seen[i]=seen[i]+1

    else:
        seen[i]=1
print(seen)
word = "apple"

seen = {}

for i in word:
    if i in seen:
        seen[i] += 1
    else:
        seen[i] = 1

print(seen)

