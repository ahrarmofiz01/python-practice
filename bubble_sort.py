nums=[5,2,8,1,9]
n=len(nums)
for i in range(n):
    swapped=False
    for j in range(n-i-1):
        if nums[j]>nums[j+1]:
            temp=nums[j]
            nums[j]=nums[j+1]
            nums[j+1]= temp
            swapped=True
    if not swapped:
        break
print(nums)
