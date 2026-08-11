def count(nums):
    count=0
    for i in nums:
        if i%2==0:
            count=count+1
    return count
answer=count([20,22,34,10,5,3,7,15,17])
print(answer)

