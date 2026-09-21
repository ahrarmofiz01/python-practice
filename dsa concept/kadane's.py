#MAXIMUM SUBARRAY
nums=[2,-3,1,-3,7,0,-9,-7,-1]
n=len(nums)
ans=nums[0]
current_sum=0
for i in nums:
    current_sum+=i
    if current_sum>ans:
        ans=current_sum
    if current_sum<0:
        current_sum=0
print(ans)