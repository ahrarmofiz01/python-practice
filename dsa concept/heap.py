#last stone weight(pririty key)
stone=[1,2,3,4,5,6]
while len(stone)>1:
    stone.sort()
    a=stone.pop()
    b=stone.pop()
    if a!=b:
        c=a-b
        stone.append(c)
if len(stone)==1:
    print(stone[0])
else:
    print("no stone weight" , 0)
