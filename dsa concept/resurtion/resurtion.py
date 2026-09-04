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
