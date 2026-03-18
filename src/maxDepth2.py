from collections import deque

class Node:
    def __init__(self,val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def maxDepth(self, root):
        if not root:
            return 0
        stack = deque()
        stack.append((root, 1))
        
        ans = 0
        while stack:
            node, depth = stack.popleft()
            ans = max(ans, depth)
            if node.left:
                stack.append((node.left, depth + 1))
            if node.right:
                stack.append((node.right, depth + 1))
        return ans
    
root = Node(0)
root.left = Node(1)
root.left.left = Node(3)
root.left.right = Node(4)
root.right = Node(2)
root.right.right = Node(5)
root.right.right.right = Node(6)

solution = Solution()
print(solution.maxDepth(root))
