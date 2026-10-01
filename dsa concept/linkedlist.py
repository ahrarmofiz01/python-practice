nums=[2,4,8,9]
target=14
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        for k in range(j+1,len(nums)):
            if nums[i]+nums[j]+nums[k]==target:
                print([i,j,k])