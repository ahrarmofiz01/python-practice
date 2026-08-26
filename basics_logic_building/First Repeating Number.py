list=[1,2,3,4,5,1]
seen={}
for i in list:
    if i in seen:
        print(i)
        break
    seen[i]=True