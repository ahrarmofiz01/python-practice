arr=[5,1,8,7,2,4,6,3]
n=len(arr)
print(n)
for i in range(n):
    for j in range(n-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
print(arr)