list=[2,3,4,6,8,10]
k=3
n=len(list)
sum=0
for i in range(k,n):
    sum=sum+list[i]
    sum=sum-list[i-k]
    print(list[i-k])
print(sum)
   