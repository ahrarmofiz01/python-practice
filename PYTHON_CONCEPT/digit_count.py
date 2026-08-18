nums=12345
count=0
while nums>0:
    nums=nums//10
    count=count+1
print(count)
nums=1234567
count=0
for i in str(nums):
    count = count+1
print(count)