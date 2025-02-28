import heapq

class Solution:
    def halfArray(self,nums):
        target = sum(nums)/2
        nums = [-num for num in nums]
        heapq.heapify(nums)
        
        ans = 0
        while target > 0:
            ans += 1
            x = heapq.heappop(nums)
            target += x/2
            heapq.heappush(nums,x/2)
        return ans

data = [5, 19, 8, 1]
solution = Solution()
print(solution.halfArray(data))
            