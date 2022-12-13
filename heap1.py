from heapq import heappush
from heapq import heappop

fruits = []

heappush(fruits, "orange")
heappush(fruits, "apple")
heappush(fruits, "banana")

print(heappop(fruits))

print(fruits)
