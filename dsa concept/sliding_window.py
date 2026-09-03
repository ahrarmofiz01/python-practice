list=[1,2,3,4,5]
k=3
sum=sum(list[:k])
for i in range(k,len(list)):
    sum=sum+list[i]-list[i-k]
print(sum)