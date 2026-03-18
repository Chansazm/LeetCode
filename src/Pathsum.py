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
        
root = PathSum(0)
root.left = PathSum(1)
root.left.left = PathSum(3)
root.left.right = PathSum(4)
root.right = PathSum(2)
root.right.right = PathSum(5)
root.right.right.right = PathSum(6)

solution = Solution()
print(solution.pathSum(root, 22))