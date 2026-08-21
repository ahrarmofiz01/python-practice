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
count=0
for i in range(1,6):
    count=count+i
print(count)
n=5
sum=0
while n>0:
    sum=sum+n
    n=n-1
print(sum)
#A for loop repeats a specific number of times, while a while loop repeats until a condition changes.
n=5
mul=1
while n>0:
    mul=n*mul
    n=n-1
print(mul)
n=5
subs=0
while n>0:
    subs=subs-n
    n=n-1
print(subs)