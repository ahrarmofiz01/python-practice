nums = [2, 7, 11, 15]
target = 9
seen = {}
for i in range(len(nums)):
    current=nums[i]
    need=target-current
    if need in seen:
        print([seen[need]], [i])
        break
    seen[current] = i
