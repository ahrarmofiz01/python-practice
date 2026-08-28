#factorial with while loop

count=1
factorial=1
while count<=5:
    factorial=factorial*count
    count=count+1

print(factorial)
for i in range(1,7):
    factorial=factorial*i
    i=i+1
print(factorial)
#with for loop
count=0
for i in range(1,50):
    count=count+i
    i=i+1
print(count)
count=10
while count>=0:
    print(count)
    count=count-1
print("boom💥")
