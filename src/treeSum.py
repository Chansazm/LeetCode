class Node:
    def __init__(self,val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def TreeSum(self,root):
        if not root:
            return 0
        left = self.TreeSum(root.left)
        right = self.TreeSum(root.right)

        return left + right + root.val


a = Node(3)
b = Node(11)
c = Node(4)
d = Node(4)
e = Node(-2)
f = Node(1)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#       3
#    /    \
#   11     4
#  / \      \
# 4   -2     1

solution = Solution()
print(solution.TreeSum(a)) # -> 21

