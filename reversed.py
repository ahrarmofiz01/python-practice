nums=123
while nums>0:
    r=nums%10
    nums//=10
    
    print(r,end="")
# iss  topic per ek or question bnane ja rhe hai jo add kregaa
nums=123
sum=0
while nums>0:
    r=nums%10
    sum= sum+r
    nums //=10
print(sum)

###############################__________________________######################################
num=121
tem=num
ans=0
while tem>0:
    r=tem%10
    if num%r==0:
        ans=ans+1
    tem//=10
print(ans)

  