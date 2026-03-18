class Solution:
    def isValidParen(self,s):
        stack = []
        matches = {"(":")","[":"]","{":"}"}
        
        for c in s:
            if c in matches:
                stack.append(c)
            else:
                if not stack:
                    return False
                current = stack.pop()
                if matches[current] != c:
                    return False
        return not stack
    

str = "({})"
solution = Solution()
print(solution.isValidParen(str))