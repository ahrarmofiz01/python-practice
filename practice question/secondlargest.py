nums = [8, 15, 15, 2, 9]
largest=nums[0]
second=nums[0]
for i in nums:
    if i>largest:
        second=largest
        largest=i
    elif i>second and i<largest:
        second=i
print(second)
print(largest)
nums = [10,20,30]
largest=nums[0]
second=nums[0]
for i in nums:
    if i>largest:
        second=largest
        largest=i
    elif i>second and i<largest:
        second=i
print(second)
print(largest)