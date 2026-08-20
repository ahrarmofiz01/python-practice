nums=[3,4,5,6,7]
count=0
for i in nums:
    if i%2==1:
        count=count+1
print(count)

num=121
temp=num
count=0
while temp>0:
    r=temp%10
    if num%r ==0:
        count=count+1
    temp=temp//10
print(count)