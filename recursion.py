
#LOOP
n=5
i=1
while i<=n:
    print(i)
    i=i+1
def printnumber(i,n):
    if i>n:
        return
    print(i)
    printnumber(i+1,n)
printnumber(1,10)
#factorial
def factorial(n):
    if n==0:
        return 1
    return n*factorial(n-1)
print(factorial(5))
