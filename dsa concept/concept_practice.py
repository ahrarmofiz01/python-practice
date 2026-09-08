num=[1,2,9,18,20]
target=38
seen={}
for i in num:
    require=target-i
    if require in seen:
        print(require,i)
    seen[i]=1
