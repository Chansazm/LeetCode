def findlength(s: str)->int:
    left = 0
    curr = 0
    ans = 0
    
    for right in range(len(s)):
        if s[right] == '0':
            curr += 1
        while curr > 1:
            if s[left] == '0':
                curr -= 1
            left += 1
        ans = max(ans, right - left + 1)
    return ans

str = "11001011"
res = findlength(str)
print(res)