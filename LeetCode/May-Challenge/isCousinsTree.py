# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        def findDepth(roots, r, i, parent):
            if roots.val == r:
                return {"a": i, "b": parent}
            i += 1
            if roots.left:
                temp1 = findDepth(roots.left, r, i, roots.val)
                if temp1:
                    return temp1
            if roots.right:
                temp2 = findDepth(roots.right, r, i, roots.val)
                if temp2:
                    return temp2

        i = 0
        one = findDepth(root, x, i, -1)
        two = findDepth(root, y, i, -1)

        if one["a"] is two["a"] and not one["b"] is two["b"]:
            return True
        else:
            return False

