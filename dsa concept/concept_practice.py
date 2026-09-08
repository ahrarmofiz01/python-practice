def power(n):
    if n==0:
        return False
    if n==1:
        return True
    if n%2==1:
        return False
    return power(n//2)
print(power(8))
