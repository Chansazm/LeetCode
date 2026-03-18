from collections import defaultdict
def longestSubString(str,k):
    left = ans = 0
    map = defaultdict(int)
    
    for right in range(len(str)):
        map[str[right]] += 1
        while len(map) > k:
            map[str[left]] -= 1
            if map[str[left]] == 0:
                del map[str[left]]
            left += 1
        ans = max(ans, right-left+1)
    return ans

str = "eceba"
print(longestSubString(str,2)) #----> 3