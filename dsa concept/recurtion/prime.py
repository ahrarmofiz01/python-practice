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
