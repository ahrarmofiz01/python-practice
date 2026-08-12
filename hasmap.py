nums=[2,3,3,2,5,6,9]
freq={}
for i in nums:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
print(freq)