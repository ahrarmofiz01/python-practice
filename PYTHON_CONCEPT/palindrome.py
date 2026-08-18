nums=121
tem=nums
count=0
while nums>0:
    digit=nums%10
    count=count*10+digit
    nums=nums//10
if count==tem:
    print("the number is palindrome")
else:
    print("not palindrome")


