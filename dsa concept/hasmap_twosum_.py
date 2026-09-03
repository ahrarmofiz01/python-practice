list=[1,2,4,5,9]
target=3
seen={}
for i in list:
    required=target-i
    if required in seen:
        print(required, i)
    seen[i]=1