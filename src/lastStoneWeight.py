import heapq

class Solution:
    def lastStoneWeight(self, stones):
        [-stone for stone in stones]
        heapq.heapify(stones)
        
        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            
            if first != second:
                heapq.heappush(stones, -(first-second))
        return stones[0] if stones else 0
        
    
    
    
    
    
    

nums = [2, 7, 4, 1, 8, 1]
solution = Solution()
x = solution.lastStoneWeight(nums)
print(x)