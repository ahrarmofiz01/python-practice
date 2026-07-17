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
#Loop Through a List
fruits=["apple","banana","cherry"]
for x in  range (len(fruits)):
    print(x)
# while loop
name=["aadam","ram","shyam"]
i=0
while i<len(name):
    print(name[i])
    i=i+1
items=["apple","orrange"]
for items in items:
    print(items,end=" ")
# function
def myfunction():
    print("hello world")
myfunction()

def add_function(a,b):
    return a+b

result = add_function(10,20)
print(result)

def mathfunction(a,b):
    return a*b
result=mathfunction(10,20)
result=mathfunction(10,300)
print(result)
input1=12345
print(input1%10)
def function(a):
    print(3.14*a*a)
function(3)

    