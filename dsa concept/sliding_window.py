list=[1,2,3,4,5]
current_sum=0
n=len(list)
k=3
for i in range(k):
    current_sum +=list[i]
ans=current_sum/k
for i in range(k,n):
    current_sum +=list[i]
    current_sum-=list[i-k]
    ans=max(ans,current_sum/k)
print(ans)


    
