import heapq

class Solution:
    def minStoneSum(self, piles, k):
        [-pile for pile in piles]
        heapq.heapify(piles)
        
        ans = 0
        ans = sum(piles)
        while k > 0:
            num = -heapq.heappop(piles)
            ans -= num
            x = num/2
            heapq.heappush(piles, -x)
            k -= 1
        return ans
        
            
    


nums = [5, 4, 9]
solution = Solution()
x = solution.minStoneSum(nums,2)
print(x)