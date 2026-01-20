def lengthOfLongestSubstring(str):
    ans = 0
    left = 0
    seen = set()
    
    for right in range(len(str)):
        while str[right] in seen:
            seen.remove(str[left])
            left += 1
        seen.add(str[right])
        ans = max(ans, right-left+1)
    return ans

s = "abcabcbb"
print(lengthOfLongestSubstring(s)) #--->3

        