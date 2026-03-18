def sum(nums,target):
    hash_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in hash_map:
            return (hash_map[complement], i)
        hash_map[num] = i
    return False

# Example usage:
nums = [2, 7, 11, 15]
target = 9
result = sum(nums, target)
print(result)  # Output: (0, 1) because nums[0] + nums[1] == 9