class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        
class Solution:
    def maxDepth(root):
        if not root:
            return 0
        stack = [(root, 1)]
        ans = 0
        
        while stack:
            ans, depth = stack.pop()
            ans = max(ans, depth)
            
            if root.left:
                stack.append(root.left, depth + 1)
            if root.right:
                stack.append(root.right, depth + 1)
        return ans