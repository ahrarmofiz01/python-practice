# a python dictionary is a collection of items ,simillar to lists and tuples.however is a key -value pair 
dict1={}
print(type(dict1))
dict1={1:"ahrar",
       2:"mohan",
       3:"aadil",
       4: "rahul"



       }
print(len(dict1))
dict1[3]="arjun"
print(dict1)
dict1.pop(3)
del dict1[4]
dict1[5]="krma"
print(dict1)
dict1[3]="baba tillu"
dict1[4]="main baba tillu"
print(dict1)
dict1={1:"ahrar",2:"mofiz",3:"aslam",4:"balgoo",5:"jiloo" }
for i in dict1:
    print(i,dict1[i])
#frequency problums
list1=[2,1,3,4,5,6,2,2,3,9,2,3]
seen={}
for i in list1:
    if i in seen:
        seen[i]=seen[i]+1
    else:
        seen[i]=1
print(seen)
# three__sum__problum
list1=[2,4,9,8,12,3,21,6]
target=39
seen={}
for i in list1:
    require=target-i
    require=require-i
    if require in seen:
        print(require,require,i)
    seen[i]=1