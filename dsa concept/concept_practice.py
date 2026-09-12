array=[0,8,2,7,9]
largest=array[0]
second=array[1]
for i in array:
    if i>largest:
        second=largest
        largest=i
print(second)
num=[0,1,3]
n=len(num)
print(n)
expextedsum=n * (n + 1) / 2
sum=0
for i in num:
    sum=sum+i
print(sum)
missingsum=expextedsum-sum
print(missingsum)