def count(nums):
    count=0
    for i in nums:
        if i%2==0:
            count=count+1
    return count
answer=count([2,9,0,12,14])
print(answer)


