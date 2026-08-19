n=[2,7,3,1,4,5,10]
target=7
for i in range(len(n)):
    for j in range(i+1,len(n)):
        if n[i]+n[j]==target:
            print([i,j])
#FINDING HOW MANY PAIRS THAT SUM=7
nums=[2,7,5,4,3,6,10,11]
target=9
count=0
for i in range(len(nums)):
    for j in range(i+1,(len(nums))):
       
        if nums[i]+nums[j]==target:
            count=count+1
print(count)
            

        