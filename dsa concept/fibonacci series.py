def fun(n):
    if n==0 or n==1:
        return n
    print(n)
    return fun(n-1)+fun(n-2)
   

fun(2)