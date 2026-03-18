from src.treeSum import Node, Solution


def build_tree():
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

    return a


def test_tree_sum():
    sol = Solution()
    assert sol.TreeSum(build_tree()) == 21


def test_empty_tree():
    sol = Solution()
    assert sol.TreeSum(None) == 0
