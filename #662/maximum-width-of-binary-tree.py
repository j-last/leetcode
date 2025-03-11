"""Below is my solution, which works but exceeded the memory limit leetcode had set.

I looked at an example solution and aim to review this problem in the future.
Hint: BFS and a formula to find the index of the left & right children of a node within their level.
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def widthOfBinaryTree(root: list[TreeNode]) -> int:
    max_width = 0
    level = [root]
    while level.count(None) != len(level):
        max_width = max(max_width, get_width(level))
        # Constructs the next level of the binary tree from the current
        # level (including all null values)
        next_level = []
        for node in level:
            if node is None:
                next_level += [None, None]
            else:
                next_level += [node.left, node.right]
        level = next_level
    return max_width


def get_width(level:list):
    """Returns the width of a level of a bianry tree.
    E.g. [None, 1, None, None, 2, None, None] would return 4.
    """
    start = None
    end = None
    for pos, item in enumerate(level):
        if item is not None and start is None:
            start = pos
        if item is not None:
            end = pos
    return end - start + 1 
        

#input = [1,3,2,5,None, None,9,6,None,7]
#root = TreeNode(1, TreeNode(3, TreeNode(5, TreeNode(6))), TreeNode(2, None, TreeNode(9, TreeNode(7))))
#print(widthOfBinaryTree(root))
