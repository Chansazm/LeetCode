import heapq
def stoneweight(nums):
    nums = [-num for num in nums]
    heapq.heapify(nums)
    print(nums)
    for num in nums:
        y = - heapq.heappop(nums)
        x = - heapq.heappop(nums)
        if x == y:
            x = 0
            y = 0
        else:
            y = y - x
            heapq.heappush(nums, -y)
        if len(nums) == 1:
            return nums[1]
    return 0

nums = [2,7,4,1,8,1]
print(stoneweight(nums)) #-->1
    
    