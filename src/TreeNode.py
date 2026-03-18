class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        
def preorder_dfs(node):
    if not node:
        return
    print(node.val)
    preorder_dfs(node.left)
    preorder_dfs(node.right)
    return
    
root = TreeNode(0)
left = root.left = TreeNode(1)
right = root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.left.right.right = TreeNode(6)
root.right = TreeNode(2)
root.right.right = TreeNode(5)

preorder_dfs(root)
