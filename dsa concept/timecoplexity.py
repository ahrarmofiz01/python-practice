for i  in range(10):
    for j in range(11):
        print(i,j)
for i in range(10*2):
    print(i)
# constant time complexity
n=100000
m=500000
#o(1)
for i in range(4):
    for j in range(3):
        print(n,m,i,j, end=" ")