class Sort:
    @staticmethod
    def sortedSquares(nums):
        n = len(nums)
        left = 0
        right = n - 1
        result = [0] * n
        
        for i in range(n-1, -1,-1):
            if abs(nums[left]) < abs(nums[right]):
                square = nums[right]
                right -= 1
            else:
                square = nums[left]
                left += 1
            result[i] = square * square
        return result
            
        
        
        
"""
Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
"""

nums = [-7,-3,2,3,11]
print(Sort.sortedSquares(nums)) #--> [4,9,9,49,121]
