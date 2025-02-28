import heapq
def halfArray(nums):
    nums = [-num for num in nums]
    nums = heapq.heapify(nums)
    T_sum = sum(nums)
    Curr_Sum = 0
        
    target = T_sum/2
    while target < Curr_Sum:
        heapq.heappop(nums)
    