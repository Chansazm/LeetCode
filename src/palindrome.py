def palindrome(word):
    right = len(word) - 1
    left = 0
    
    
    while left < right:
        if word[left] != word[right]:
            return False
        left += 1
        right -= 1
    return True







print(palindrome("racear")) #-->True