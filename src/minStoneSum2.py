

class Solution:
            
    def minStoneSum2(self, nums, k):
        map = {}
        for i,v in nums:
            map[i] = v
        
        Max = -'inf'
        
        for k, v in enumerate(map):
            if v > Max:
                Max = v
                
        
        return abs(sum(data))



nums = [5, 4, 9]
solution = Solution()
x = solution.minStoneSum2(nums,2)
print(x)