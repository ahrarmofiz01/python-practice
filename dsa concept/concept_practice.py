#concept practice
def num(n):
    if n==0:
        return False
    if n==1:
        return True
    if n%2==1:
        return False
    return  num(n//2)
print(num(2))
  
