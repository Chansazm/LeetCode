import heapq

class MedianFinder:
    def __init__(self):
        self.min_heap = []
        self.max_heap = []
        
    def findMedian(self):
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        return self.max_heap[0] - self.min_heap[0]/2
    
    def addNum(self, num):
        heapq.heappush(self.max_heap, -num)
        heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        
        if len(self.min_heap) > len(self.max_heap):
            x = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -x)
        return