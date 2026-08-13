nums=[1,2,1,3,4,3,9,9,9,9,9,9,9,9,9]
freq={}
for i  in nums:
    if i in freq:
        freq[i] +=1
    else:
        freq[i]=1
print(freq)
