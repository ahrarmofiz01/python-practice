#lonest strike
nums=[1,2,3,2,3,4,5,6,5,7]
current=1
largest=1
for i in range(1,len(nums)):
    if nums[i]>nums[i-1]:
        current=current+1
        if current>largest:
            largest=current
    else:
        current=1
print(largest)