from collections import Counter

class Stack:
    def __init__(self):
        self.data = []
    def is_empty(self, nums):
        return len(self.data) == 0
    
    def length(self):
        len(self.data)

class Solution:
    def topkfrequent(self, nums, k):
        count = {}
        for val in (nums):
            if val in count:
                count[val] += 1
            else:
                count[val] = 1
        #print(count)
        #Stack.is_empty(count)
        print(Stack().is_empty(count))
        print(Stack().length())
    
    
solution = Solution()

arr = [1, 1, 1, 2, 2, 3]
solution.topkfrequent(arr, 2)
        