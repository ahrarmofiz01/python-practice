n=[1,2,3,4,5]
k=2
p=len(n)
print(p)
sum=0
for i in range(k):
    sum=sum+n[i]
ans=sum/2
for i in range(k,p):
    sum= sum+n[i]
    sum=sum-n[i-k]
    ans=max(ans,sum/2)
print(ans)
