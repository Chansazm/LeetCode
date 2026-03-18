class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def issametree(self,p,q):
        stack = [(p,q)]
        
        while stack:
            p, q = stack.pop()
            
            #if both trees are empty
            if not p and not q:
                return True
            #if tree values are different
            if q.val != p.val:
                return False
            #if either tree is empty but not both
            if not q or not p:
                return False
            stack.append((p.right,q.right))
            stack.append((p.left,q.left))
        return True
    
root = TreeNode(0)
root.left = TreeNode(1)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right = TreeNode(2)
root.right.right = TreeNode(5)
root.right.right.right = TreeNode(6)

solution = Solution()
print(solution.issametree(root.left.right,root.right))