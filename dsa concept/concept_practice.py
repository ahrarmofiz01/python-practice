def num(n):
    if n==11:
        return n
    print(n)
    num(n+1)
num(1)

numbers = [4, 2, 4, 3, 2, 4, 5, 3, 2, 2, 5, 5, 5]
seen={}
for i in numbers:
    if i in seen:
        seen[i]=seen[i]+1
    else:
        seen[i]=1
print(seen)
