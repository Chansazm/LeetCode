import heapq

heap = [67, 341, 234, -67, 12, -976]
#heapify
heapq.heapify(heap)
heapq.heappush(heap,9090)

#print heap
while heap:
    print(heapq.heappop(heap))
    