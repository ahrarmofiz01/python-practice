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