set1={9,2,3,4,6,1,7}
print(set1)
set1={"hello",100,20.89,"hiii",100}
print(set1)
print(len(set1))
print(type(set1))
set1.add("hello world")
print(set1)

set2=set1.copy()
print(set2)
set2.add("name")
print(set2)
set2.discard(100)
print(set2)
set1={1,3,5,8,9}
set2={9,5,11,28,1}
print(set1^set2)
#or
print(set1.union(set2))