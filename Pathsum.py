class PathSum:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        
class Solution:
    def pathSum(self,root,targetSum):
        def dfs(node, curr):
            curr += node.val
            
            if node.left == None and node.right == None:
                return (curr + node.val) == targetSum
                
            
            left = dfs(node.left, curr)
            right = dfs(node.right, curr)
            
            return left or right
        return dfs(root, 0)
            