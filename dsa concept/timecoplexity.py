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
#quadratic time (o(n^2))
n=10
for i in range(n**2):
    print(i)
#o(n^2)
####################################################
#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
#__________________________________________________#
#0(log2n) opration
n=100
i=1
while i<=n:
    print(i,end=" ")
    i=i*2