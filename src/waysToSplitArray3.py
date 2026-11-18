class Solution:
    def waysToSplitArray(self,nums):
        n = len(nums)
        prefix_sum = [0] * n
        prefix_sum[0] = nums[0]

        for i in range(1, n):
            prefix_sum[i] = (prefix_sum[-1]+ nums[i])

        ans = 0
        for i in range(n - 1):
            left_section = prefix_sum[i]
            right_section = prefix_sum[-1] - prefix_sum[i]
            if left_section > right_section:
                ans += 1
        return ans


array = [10,4,-8,7]
solution = Solution()
result = solution.waysToSplitArray(array) #---> 2
print(result)

