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
#with munctiom
import heapq
def stone(list):
    heap=[]
    for i in list:
        heapq.heappush(heap,-i)
    while len(heap)>1:
        a=-heapq.heappop(heap)
        b=-heapq.heappop(heap)
        if a!=b:
            heapq.heappush(heap,-(a-b))
    if len(heap)>0:
        return -heap[0]
    else:
        return 0
print(stone([1,2,3,4,5,6]))