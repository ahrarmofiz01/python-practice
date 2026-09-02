dict1={}
print(type(dict1))
dict={1:'ahrar',2:'ali',3:'golu'}
print(dict)
dict[3]="alikhan"
dict.update({4:"hello",5:"hi"})
print(dict)
for i in dict:
    print( i,dict[i])
#### frequency question#########
list1=[1,2,3,4,5,6,1]
freq={}
for i in list1:
    if i in freq:
        freq[i]=freq[i]+1
    
print(freq)
    