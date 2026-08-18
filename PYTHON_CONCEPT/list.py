nums=[2,3,4,5,6]#this is a list
print(nums)
print(nums[0])#access list items
#indexing
print(nums[-1])#negative
print(nums[2:4])#[start : stop] → start included, stop excluded
#stop value is not included
print(nums[:3])
print(nums[-3:-1])
if 4 in nums:#Check if Item Exists
    print(True)
else:
    print(False)
nums.append(10)
print(nums)
nums.pop()#first 10
print(nums)
nums.pop()#then 6
print(nums)
nums.insert(0,"banana")
print(nums)
nums.reverse()
print(nums)
nums.pop()
nums.sort()
print(nums)