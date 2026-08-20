nums=1234
reversed=0
while nums>0:
    r=nums%10
    reversed=reversed*10+r
    nums=nums//10
print(reversed)
