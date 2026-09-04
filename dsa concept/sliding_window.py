list=[2,4,6,8,10,12]
k=3
n=len(list)
sum=0
for i in range(k):
    sum=sum+list[i]
    print(sum)
ans=sum
for i in range(k,n):
    sum=sum+list[i]
    sum=sum-list[i-k]
    ans=max(ans,sum)
   


