def find_largest(nums):
    largest = nums[0]

    for i in nums:
        if i > largest:
            largest = i

    return largest
answer=find_largest([8,9,1021,19])
print(answer)

