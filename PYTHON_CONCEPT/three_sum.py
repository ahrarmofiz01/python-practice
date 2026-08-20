nums=[1,1,1,5,9,10]
target=3
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        for k in range(j+1,len(nums)):
            if nums[i]+nums[j]+nums[k]==target:
                print([i,j,k])


