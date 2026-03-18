from math import sqrt
import heapq

class Solution:
    def kClosest(self, nums, k):
        distance = 0
        heap = []
        for arr in nums:
            x, y = arr
            distance = (x-0)**2 + (y-0)**2
            distance = sqrt(distance)
            heapq.heappush(heap, (distance, arr))
        #print(heap)
        array = []
        for item in range(k):
            item = heapq.heappop(heap)
            distance, arr = item
            array.append(arr)
            
        return array
            
        
              
        
nums = [[1,3],[2,-2]]    
k = 1  
solution = Solution()
x = solution.kClosest(nums,k)
print(x) #---> [-2,2]
