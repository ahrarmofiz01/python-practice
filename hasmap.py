nums=[2,4,5,2,8,3]
freq={}
for i in nums:
    if i in freq:
        freq[i] +=1
    else:
        freq[i]=1
print(freq)
