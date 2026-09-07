#cheking number is prime or not
def primenum(n):
    if n==0 or n==1:
        return False
    for i in range(2,n):
        if n%i==0:
           return  False

    return True
print(primenum(3))
#sieve of eratosthenes
n=10
prime=[True]*(n+1)
prime[0]=False
prime[1]=False
for i in range(2,n+1):
    if prime[i]:
        for j in range(2*i,n+1,i):
            prime[j]=False
for i in range(n+1):
    if prime[i]:
        print(i)
