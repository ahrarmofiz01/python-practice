list=[1,2,3,4,5,6,7]
k=3
n=len(list)
sum=0
for i in range(k):
    sum=sum+list[i]
    print(sum)
ans=sum/k
for i in range(k,n):
    sum=sum+list[i]
    sum= sum-list[i-k]
    ans=max(sum/k,ans)
print(ans)

   


