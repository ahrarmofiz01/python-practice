#with loop
def poweroftwo(n):
    if n==0:
        return False
    while n%2==0:
        n=n/2#n/=2 v likh skte hai 
    return n==1
print(poweroftwo(0))
# with recurtion
def poweroftwo(n):
    if n==0:
        return False
    if n==1:
        return True
    if n%2==1:
        return False
    return poweroftwo(n//2)
print(poweroftwo(8))
