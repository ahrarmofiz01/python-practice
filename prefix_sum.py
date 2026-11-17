arr=[1,2,3,4,5]
# output=[1,3,6,10,15]
list=[]
sum=0
for i in arr:
    sum=sum+i
    list.append(sum)
print(list)
ans=0
for i in range(1,4):
    ans=ans+arr[i]
    
print(ans)
   