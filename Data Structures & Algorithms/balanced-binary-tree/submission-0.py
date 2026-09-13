# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalancedWithHeight(self, root):
        if root == None:
            return (0, True)
        else:
            left_height, left_balanced = self.isBalancedWithHeight(root.left)
            right_height, right_balanced = self.isBalancedWithHeight(root.right)
            balanced = abs(left_height - right_height) <= 1 and left_balanced and right_balanced
            return (max(left_height, right_height) + 1, balanced)
            

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        _, balanced = self.isBalancedWithHeight(root)
        return balanced