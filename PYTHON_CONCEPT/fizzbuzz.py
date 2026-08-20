nums=[3,5,9,15,18,20,2,22]
list=[]
for i in nums:
    if i%5==0 and i%3==0:
        list.append("fizzbuzz")

    elif i%3==0:
        list.append("buzz")
    elif i%5==0:
        list.append("fizz")
    else:
        list.append(str(i))

print(list)
