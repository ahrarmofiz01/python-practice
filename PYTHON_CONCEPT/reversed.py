nums=12345
count=0
while nums>0:
    digit=nums%10
    count=10*count+digit
    
    nums=nums//10
print(count)
