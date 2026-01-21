class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p, q):
        #if both trees are empty, they are the same
        if not p and  not q:
            return True
        #if values are not equal, they are not the same tree
        if p.val != q.val:
            return False
        #if either tree is empty, they are not the same
        if not p or not q:
            return False
        left = self.isSameTree(p.left, q.left)
        right = self.isSameTree(p.right, q.right)
        
        return left and right
    
root = TreeNode(0)
root.left = TreeNode(1)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right = TreeNode(2)
root.right.right = TreeNode(5)
root.right.right.right = TreeNode(6)

solution = Solution()
print(solution.isSameTree(root.left.right,root.right))