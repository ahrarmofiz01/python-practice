nums=424
tem=nums
reversed=0
while nums>0:
    r=nums%10
    reversed=reversed*10+r
    nums=nums//10
print(reversed)
if tem==reversed:
    print("the number  pelendrome")
else :
    print("number is not pelendrome")

