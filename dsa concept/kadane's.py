#MAXIMUM SUBARRAY
nums=[-2,1,-3,4,-1,2,1,-5,4]
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