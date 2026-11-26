nums=[2,3,56,1]
largest=nums[0]
for i in range(len(nums)):
    if nums[i]>largest:
        largest=nums[i]
        print(largest)


nums=[2,3,56,55,1]
largest=nums[0]
second=nums[1]
for i in range(len(nums)):
    if nums[i]>largest:
        second=largest
        largest=nums[i]
    elif nums[i]>second and nums[i]<largest:
        second=nums[i]
print(second)
  
