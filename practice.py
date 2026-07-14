#factorial question solution
num=1
count=1
while count<=5:
    num=num*count
    count=count+1
print(num)
#list
list=["apple","banana","cherry","orange","kiwi"]
print(list)
num=[10,20,30]
print(num)
num.append(40)
print(num)
num.insert(0,5) #Add 5 at the beginning.
print(num)
num.remove(20)
print(num)
#find sum and avrage
marks=[10,20,30,40,50]
total=sum(marks)
print(total)
avrage=total/len(marks)
print(avrage)