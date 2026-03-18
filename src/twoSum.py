def twoSum(nums, target):
    map = {}
    for k,v in enumerate(nums):
        difference = target - v
        if difference in map:
            return [map[difference],k]
        map[v] = k
    return []

nums = [2,7,11,15]
target = 9


print(twoSum(nums, target)) # 0, 1