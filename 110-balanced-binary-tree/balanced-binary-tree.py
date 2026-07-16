# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def __init__(self):
        self.ans = True

    def maxHeight(self, root: Optional[TreeNode]) -> int:

        if root == None:
            return 0
        
        leftHeight = self.maxHeight(root.left)
        rightHeight = self.maxHeight(root.right)

        if abs(leftHeight - rightHeight) > 1:
            self.ans = False

        return max(leftHeight, rightHeight) + 1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        self.maxHeight(root)
        return self.ans
        