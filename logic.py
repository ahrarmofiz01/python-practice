nums=[0]


largest=nums[0]
for i in range(len(nums)):
    if nums[i]>largest:
        largest=nums[i]
print(largest)


nums=[2,3,55,55,1]
largest=nums[0]
second=nums[1]
for i in range(len(nums)):
    if nums[i]>largest:
        second=largest
        largest=nums[i]
    elif nums[i]<largest and nums[i]>second:
        second=nums[i]
print(second)
nums=[2,3,55,55,1] 
sum=0
for i in nums:
    sum=sum+i
print(sum)
num=int(input("enter your number:"))
i=2
if num<=1:
    print("not prime")
else:
    while i*i<= num:
        
        if num%i==0:
            print("not prime")
            break
        i=i+1
    else:
        print("prime")




        


