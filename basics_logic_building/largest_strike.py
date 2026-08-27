#longest strike
score=[0,1,2,1,2,3,4,5,4,2]
current=1
largest=1
for i  in range(1,len(score)):
    if score[i]>score[i-1] :
        current=current+1
        if current>largest:
            largest=current
    else:
        current=1
print(largest)

    

    