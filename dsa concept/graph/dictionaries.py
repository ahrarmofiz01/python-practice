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
list=[1,2,3,4,1,2,2]
freq={}
for i in list:
    if i in freq:
        freq[i]=freq[i]+1
    else:
        freq[i]=1
for i in freq:
    print(freq[i],i)
    

    