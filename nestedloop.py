for i in range(1,5):
    for j in range(i,5):
        print(i,j)
    print("hello")
# i ki value tab tak same rahegi jab tak j ka loop complete nahi hota.
#j har iteration mein apni value change karega.Agar print(i, j) hai, toh i baar-baar print hoga, kyunki print statement inner loop ke andar hai.



#Agar print(i) inner loop ke bahar hai, toh i sirf ek baar print hoga per outer iteration.
#OUTPUT
#1 1
#1 2
#1 3
#1 4
#2 2
#2 3
#2 4
#3 3
#3 4
#4 4
for i in range(1, 5):
    for j in range(1, 6):
        print("#", end="")
    print()
for i in range(2):
    print(i)
    for j in range(10,13):
        print(j)
#print the multiplication  Table of 2
for i in range(2,3):
    for j in range(1,11):
        print(i,"*",j,"=",i*j)
# print a simple triangle pattern.
rows=5
for i in range(1,rows+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
##############################################
for i in range(6,0,-1):
    for j in range(1,i-1):
        print(i,j,end=" ")
    print()

    