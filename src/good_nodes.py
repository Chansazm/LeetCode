class TreeNode:
    def __init__(self,val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def good_nodes(self,root):
        def dfs(root, max_so_far):
            if not root:
                return 0
            ans = 0
            left = dfs(root.left, max(max_so_far,root.val))
            right = dfs(root.right,max(max_so_far,root.val))
            ans = left + right
            
            if root.val > max_so_far:
                ans += 1
            return ans
        return dfs(root, float('-inf'))
    
    
root = TreeNode(0)
root.left = TreeNode(1)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right = TreeNode(2)
root.right.right = TreeNode(5)
root.right.right.right = TreeNode(6)

solution = Solution()
print(solution.good_nodes(root))



        

            
        