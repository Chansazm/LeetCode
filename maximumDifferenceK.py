class Solution:
    def maximumDifferenceK(self, nums, k):
        nums.sort()
        ans = 1
        x = nums[0]
        for i in range(len(nums)):
            if nums[i] - x > k:
                x = nums[i]
                ans += 1
                
        return ans
    

k = 2
nums = [3,6,1,2,5]
solution = Solution()
print(solution.maximumDifferenceK(nums,k))