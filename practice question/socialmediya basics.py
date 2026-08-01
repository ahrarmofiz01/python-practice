a = 20
b = "20"

print(a != b)
a = "30"
b = 20

#print(a > b)#error
#a = "50"

#b = "40"

#print(a > b)
a = "50"
b = "40"

print(a > b)
#true
print("100" > "99")
a=[1,2,3,4,5]
print(a*2)
b=[1,2,3,4,5]
print(b*0)#ye concept main hmne sikhaa zero ko chod kr baaki kisi v number say multiply krte hai tb utnee time repit hota hai likne zero say multiply krne say ek null list milta hai
nums=[12,5,8,7,20]
list=[]
for i in nums:
    if i%2==1:
        list.append(i)
print(list)
print(list[0]+list[1]) #BAD METHOD NOT GOOD🤣

nums = [12, 5, 8, 7, 20]

total = 0

for i in nums:
    if i % 2 == 1:
        total = total + i

print(total)
j=[2,5,9,8,4,12]
sum=0 
for i in j:
    if i%2==0:
        sum=sum+i

print(sum)
k=[2,3,4,5,6,9]
sum=0
for i in k:
    if i>=5:
        sum=sum+i
print(sum)

    