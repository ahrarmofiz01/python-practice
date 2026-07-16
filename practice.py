#factorial question solution
num=1
count=1
while count<=5:
    num=num*count
    count=count+1
print(num)
#list
#find sum and avrage
marks=[10,20,30,40,50]
total=sum(marks)
print(total)
avrage=total/len(marks)
print(avrage)
#second largest number
marks=[99,20,30,80]
marks.sort()
print(marks[-2])
this_list=[99,22,33,22,33]
if 99 in this_list:
    print("true")
name=["ahrar","ali","ahmed","orange"]
if "orange" in name:
    name.remove("orange")
    print(name)
#add list items
list1=["ahrar","ali","ahmed"]
list1.append("akram")
print(list1)
list1.insert(0,"mofiz")
print(list1)
list2=[34,42,99,1,2,3,4]
list3=[34,92,88,12,43]
list2.extend(list3)
print(list2)
print(sorted(set(list2)))