nums = [100,4,200,1,3,2]
set1=set(nums)
print(set1)
max_strike=0
for i in set1:
    if i-1 not in set1:
        j=i
        current_strike=1
        while j+1 in set1:
            j+=1
            current_strike+=1
        max_strike=max(max_strike,current_strike)


print(max_strike)

