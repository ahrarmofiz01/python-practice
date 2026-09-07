def poweroftwo(n):
    while n%2==0:
        n/=2
    return n==1
print(poweroftwo(16))
