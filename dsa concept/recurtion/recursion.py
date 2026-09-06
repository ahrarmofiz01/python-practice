#loop
i=0
while i<5:
    print(i)
    i+=1
#output=0,1,2,3,4


#recursion

def function(i):
    if i==5:
        return
    print(i)
    function(i+1)
function(0)




def fun2(x,n):
    if x==n:
        return
    print(n)
    fun2(x,n-2)
fun2(0,10)
##RECURSIVE STACK
def fun3(i):
    if i==5:
        return
    fun3(i+1)
    print(i)
fun3(1)


def fun3(j):
    if j==5:
        return
    print(j)
    fun3(j+1)
fun3(0)
### factorial #####
def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)
print(fact(5))
#GCD
def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)
print(gcd(10,5))

def gcd1(c,d):
    if d==0:
        return c
    return gcd1(d,c%d)
print(gcd1(9,3))

