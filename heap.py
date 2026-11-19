import heapq
from multiprocessing import heap
h=[]
heapq.heapify(h)
heapq.heappush(h, 5)
heapq.heappush(h, 1)
heapq.heappush(h, 3)
heapq.heappush(h, 4)
print(heapq.nsmallest(3, h))