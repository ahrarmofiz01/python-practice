def num(n):
    if n==11:
        return n
    print(n)
    num(n+1)
num(1)

numbers = [7, 2, 7, 3, 2, 7, 4, 3, 2, 2, 5, 4, 7]
seen={}
for i in numbers:
    if i in seen:
        seen[i]=seen[i]+1
        
    else:
        seen[i]=1
print(seen)
largest=0
largest_key=None
for kew ,value in seen.items():
    if value>largest:
        largest=value
        largest_key=kew
print(largest_key,largest)
numbers = [4, 7, 2, 9, 5, 8]

largest = 0
second = 0

for i in numbers:

    if i > largest:
        second = largest
        largest = i

    elif i > second:
        second = i

print("Largest:", largest)
print("Second Largest:", second)
