def flipzero(str):
    left = right = curr = ans = 0
    n = len(str)
    
    for right in range(n):
        if str[right] == '0':
            curr += 1
        while curr > 1:
            if str[left] == '0':
                curr -= 1
            left += 1
        ans = max(ans, right - left + 1)
    return ans


s = "1101100111"
st = flipzero(s) #--> 5
print(st)
        
        
        