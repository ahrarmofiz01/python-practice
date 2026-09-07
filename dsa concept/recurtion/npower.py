#with loop
#power of four and power of two 
def poweroftwo(n):
    if n==0:
        return False
    while n%4==0:
        n=n/4#n/=2 v likh skte hai 
    return n==1
print(poweroftwo(5))
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
