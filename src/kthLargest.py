import heapq

class KthLargest:

    def __init__(self, k, nums):
        self.min_heap = nums
        self.k = k
        heapq.heapify(nums)
        
        while len(nums) > k:
            heapq.heappop(nums)
           

    def add(self, val):
        heapq.heappush(nums, val) 
        if len(nums) > k:
            heapq.heappop(nums) hu
        return nums[0]                                      
             
k = 3
nums = [4,5,8,2]     
solution = KthLargest(k, nums)
print(solution.add(3)) #-----> 4
        