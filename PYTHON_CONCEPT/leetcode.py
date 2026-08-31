#######Count the Digits that Divide the Number#####
num=121
temp=num
count=0
while temp>0:
    r=temp%10
    if num%r ==0:
        count=count+1
    temp=temp//10
print(count)