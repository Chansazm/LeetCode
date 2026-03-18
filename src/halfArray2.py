import heapq

class Solution:
    def halfArray(self, nums):
        heap = [-num for num in nums]
        heap = heapq.heapify(heap)
        target = sum(nums)/2
        
        ans = 0
        while target > 0:
            ans += 1
            max = heapq.heappop(heap)
            heapq.heappush(heap,max/2)
        return ans
    

nums = [5,19, 8, 1]    
solution = Solution().halfArray(nums)
print(solution) #--> 