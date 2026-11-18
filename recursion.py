
#LOOP
n=5
i=1
while i<=n:
    print(i,end=" ")
    i=i+1
def printnumber(i,n):
    if i>n:
        return
    print(i,end=" ")
    printnumber(i+1,n)
printnumber(1,10)