# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root):
        if root == None:
            return -1
        else:
            left = self.maxDepth(root.left)
            right = self.maxDepth(root.right)

            depth = max(left, right) + 1
            diameter_subtree = left + 1 + right + 1
            print(depth, diameter_subtree)

            self.diameter = max(self.diameter, depth)
            self.diameter = max(self.diameter, diameter_subtree)

            return depth

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        self.maxDepth(root)

        return self.diameter