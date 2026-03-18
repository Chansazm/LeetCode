def consecutiveones2(str):
    left = curr = ans = 0
    
    for right in range(len(str)):
        if str[right] == '0':
            curr += 1
        while curr > 1:
            if str[left] == '0':
                curr -= 1
            left += 1
        ans = max(ans, right - left + 1)
    return ans

s = "1101100111"
print(consecutiveones2(s)) #--> 5