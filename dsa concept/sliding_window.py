list=[1,2,3,4,5,6]
k=2
sum=0
for i in range(k):
    sum+=list[i]
ans=sum/k
for i in range(k,len(list)):
    sum+=list[i]
    sum-=list[i-k]
    ans=max(ans,sum/k)
print(ans)


    
