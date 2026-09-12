#concept practice
def pow(n):
    if n==0:
        return False
    if n==1:
        return True
    if n%2==1:
        return False
    return pow(n//2)
print(pow(8))
#sliding window question
list=[1,2,3,4,5]
n=len(list)
k=2
sum=0
for i in range(k):
    sum=sum+list[i]
print(sum)
for i in range(k,n):
    sum=sum+list[i]
    sum= sum-list[i-k]
print(sum)
  
