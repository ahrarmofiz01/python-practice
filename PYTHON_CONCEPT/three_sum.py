nums = [0, 1, 7, 1, 3]
target = 9
for i in range(len(nums)):
    for j in range (i+i,len(nums)):
        for k in range(j+1,len(nums)):
            if nums[i]+nums[j]+nums[k]==target:
                print([i,j,k])
