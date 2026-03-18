def twosum(nums, target ):
    map = {}
    
    for i, v in enumerate(nums):
        map[i] = v
        
        # difference = target - v
        # if difference in map:
        #     return [i, map[difference]]
    return map

nums = [2,7,11,15]
target = 9


print(twosum(nums, target)) # 0, 1