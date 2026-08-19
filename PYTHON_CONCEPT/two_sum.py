n=[2,7,3,1,4,5,10]
target=7
for i in range(len(n)):
    for j in range(i+1,len(n)):
        if n[i]+n[j]==target:
            print([i,j])

        