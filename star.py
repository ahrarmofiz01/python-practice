for i in  range(1,11):
    print(i)
n=10
if n%2==0:
    print("n is even")
else:
    print("odd")

count=0
while count<=100:
    print(count)
    count=count+2
for i in range(1,11):
    print(i*7)
num=1
count=1
while count<=5:
    num=num*count
    count=count+1
print(num)
n=7
for i in range(1,11):
    print(n,"x",i,"=",n*i)
number=12
for i in range(1,11):
    if 12%i==0:
        print(i,"this is the factor")
list=[1,9,8,7]
largest=list[0]
for i in list:
    if i>largest:
        largest=i
print(largest)
nums = [2, 5, 8, 1, 10]
total = 0

for i in nums:
    if i%2==0:
        total = total+i
print(total)