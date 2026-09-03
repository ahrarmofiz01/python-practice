list=[1,2,3,4,5]
k=3
sum=sum(list[:k])
max_sum=sum
average=sum/k
max_average=average
for i in range(len(list)-k):
    sum=sum-list[i]+list[i+k]
    max_sum=max(max_sum,sum)
    max_average=max(max_average,sum/k)
    print(max_average)

    
