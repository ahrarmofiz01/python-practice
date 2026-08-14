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
