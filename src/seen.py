def seen(s):
    seen = set()
    for i in range(len(s)):
        c = s[i]
        if c in seen:
            return True
        seen.add(c)
    return False
    
    
    
    
    
    
s = "abcdeda"
print(seen(s)) #---> T