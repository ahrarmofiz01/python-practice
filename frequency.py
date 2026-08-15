nums=9191
tem=nums
sum_=0
product=1
while tem>0:
    r=tem%10
    tem//=10
    sum_+=r
    product*=r
print(product-sum_)
num = 121
temp = num
reverse = 0

while temp > 0:
    r = temp % 10
    reverse = reverse * 10 + r
    temp = temp // 10

if num == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")
candie=[1,2,3,4,5,6]
extracandie=3
maxcandie=max(candie)
ans=[]
for i in candie:
    if (i+extracandie)>maxcandie:
        ans.append(True)
    else:
        ans.append(False)
print(ans)
nums = [5, 8, 2, 15, 7, 1]

largest = nums[0]   # Assume first element is the largest

for i in nums:
    if i > largest:
        largest = i

print("Largest number is:", largest)
#minimum number
nums=[3,4,6,1,7,8,9]
lowest=nums[0]
for i in nums:
    if i<lowest:
        lowest=i
print(lowest)