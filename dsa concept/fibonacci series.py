def febonacci(n):
    if n==0 or n==1:
        return n
    return febonacci(n-1)+febonacci(n-2)
print(febonacci(4))