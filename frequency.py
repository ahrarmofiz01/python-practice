num=234
tem=num
sum_=0
product=1
while tem>0:
    r= tem%10
    tem//=10
    sum_+=r
    product*=r
print(product-sum_)
