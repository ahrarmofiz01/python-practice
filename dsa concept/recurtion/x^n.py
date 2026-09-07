def mypow(x,n):
    if n==0  :
        return 1
    if n<0:
        n*=-1
        return 1/mypow(x,n)
   
    if n==1:
        return x
    a=mypow(x,n//2)
    if n%2==1:
        return a*a*x
    else:
        return a*a
    
#power>=0
print(mypow(2,-2))
def power(x,n):
    if n==0:
        return 1
    if n==1:
        return x
    a=power(x,n//2)
    if n%2==1:
        return a*a*x
    else:
        return a*a
print(power(2,3))

