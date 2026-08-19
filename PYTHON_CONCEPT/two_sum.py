n=[2,8,7,9,10]
target=9
for i in range(len(n)):
    for j in range(i+1,len(n)):
        if n[i]+n[j]==target:
            print([i,j])

        