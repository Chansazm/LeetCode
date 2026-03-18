def find_numbers(nums):
    ans = []
    set = set(nums)
    
    for num in nums:
        if num - 1 not in set or num + 1 not in set:
            ans.append(num)
    return ans

