array=[0,8,2,7,9]
largest=array[0]
second=array[1]
for i in array:
    if i>largest:
        second=largest
        largest=i
print(second)
  
