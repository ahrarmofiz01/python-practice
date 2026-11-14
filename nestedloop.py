for i in range(1,5):
    for j in range(i,5):
        print(i,j)
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