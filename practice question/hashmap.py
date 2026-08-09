nums=[5,5,3,12]
target=10
seen={}
for i in range(len(nums)):
    current=nums[i]
    need=target-current
    if need in seen:
        print([seen[need],i])
        break
    seen[current]=i

nums=[9,1,2,3,4]
target=5
seen={}
for i  in range(len(nums)):
    current=nums[i]
    need=target-current
    if need in seen:
        print([seen[need],i])
        break
    seen[current]=i
nums = [3, 8, 5, 3, 9, 8]
seen={}
for i  in range(len(nums)):
    current=nums[i]
    if current in seen:
        print(current)
        break
    seen[current]=i

