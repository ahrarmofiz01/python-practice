data=[1,2,3,4,5,6,7]  
k=3
n=len(data) 

sum=0
for i in range(k):
    sum=sum+data[i]
ans=sum/k
for i in range (k,n):
    sum=sum+data[i]
    sum=sum-data[i-k]
    ans=max(ans,sum/k)
print(ans)