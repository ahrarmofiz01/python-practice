list=[1,2,3,4,5,1]
seen={}
for i in list:
    if i in seen:
        print(i)
        break
    seen[i]=True
    nums=[1,1,1,2,2,3,4,5,5,6,6]
    freq = {}

for i in nums:

    if i in freq:
        freq[i] = freq[i] + 1
    else:
        freq[i] = 1

print(freq)