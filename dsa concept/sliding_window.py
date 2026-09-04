list=[2,4,6,8,10,12]
k=3
n=len(list)
print(n)
sum=0
for i in range(k,n):
    sum=sum+list[i]
    sum=sum-list[i-k]
print(sum)
