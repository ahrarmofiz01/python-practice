array=[2,3,3,4,2,8,9,3,7,2,2,2,2,2,2,2,22,2]
count=0
num=array[0]
for i in array:
    if num==i:
        count= count+1
print(num,"frequency = ",count)
   