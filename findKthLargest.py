import heapq

class Solution:
    def findKthLargest(self, nums, k):
        nums = [-num for num in nums]
        heapq.heapify(nums)
        
        i = 1
        while i < k:
            curr = heapq.heappop(nums)
            
            i += 1
        return abs(curr)

# nums = [3, 2, 1, 5, 6, 4]
# k = 2

nums = [3,2,3,1,2,4,5,5,6]
k = 4

solution = Solution()
ans = solution.findKthLargest(nums, k)
print(ans)
            
            