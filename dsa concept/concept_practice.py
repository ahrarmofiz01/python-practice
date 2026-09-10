#power of n
def pow(n):
    if n==1:
        return True
    if n==0:
        return False
    if n%2==1:
        return False
  
    return pow(n//2)
print(pow(16))
#continiu number
def num(n):
    if n==5:
        return
    print(n)
    num(n+1)
num(0)