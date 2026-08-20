nums=[10.20,39,0,0.123,10101928838737373,980,43048,3930,99764]
largest=nums[0]
for i in nums:
    if i>largest:
        largest=i
print(largest)
nums=[10,20,9,30,40]
for i in nums:
    if i%3==0:
        print(i)
num=5
count=1
sum=0
while num>0:
    sum=sum+count
    count=count+1
    num=num-1
print(sum)