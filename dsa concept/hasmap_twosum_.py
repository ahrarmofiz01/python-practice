list=[2,9,12,15,21]
target=11
seen={}
for i in list:
    require=target-i
    if require in seen:
        print(require,i)
    seen[i]=1
 
 
 