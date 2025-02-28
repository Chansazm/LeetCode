class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self,root):
        if not root:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        
        return max(left, right) + 1

root = Node(0)
root.left = Node(1)
root.left.left = Node(3)
root.left.right = Node(4)
root.right = Node(2)
root.right.right = Node(5)
root.right.right.right = Node(6)

solution = Solution()
solution.maxDepth