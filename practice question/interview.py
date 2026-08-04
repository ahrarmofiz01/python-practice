nums = [5, 8, 12, 3, 10]
sum=0
for i in nums:
    if i%2==0:
        sum=sum+i
print(sum)
nums = [2, 7, 10, 15, 20]
count=0
for i in nums:
    if i%5==0:
        count=count+1
print(count)
nums = [11, 4, 8, 25]
found=False
for i in nums:
    if i==25:
        found=True
print(found)
nums = [22,18,15]
largest=nums[0]
for i in nums:
    if i>largest and i%2==1:
        largest=i
print(largest)