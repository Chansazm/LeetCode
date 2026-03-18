class targetSum:
    def targetsum(nums, target):
        i = 0
        j = len(nums) - 1
        sum = 0
        
        while i < j:
            sum = nums[i] + nums[j]
            if sum == target:
                return True
            if sum > target:
                j -= 1
            else:
                i += 1
            
        return False
            
            
nums = [1,2,4,6,8,9,14,15]           
print(targetSum.targetsum(nums,13))