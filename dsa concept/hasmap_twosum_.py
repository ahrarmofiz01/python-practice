list=[12,3,9,9,19]
target=18
seen={}
for i in  list:
    require=target-i
    if require in seen:
        print(require,i)
    seen[i]=1
 
 
 