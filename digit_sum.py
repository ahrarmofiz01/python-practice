nums=12345
total_sum=0
while nums>0:
    digit=nums%10
    total_sum=total_sum+digit
    nums=nums//10
print(total_sum)

        