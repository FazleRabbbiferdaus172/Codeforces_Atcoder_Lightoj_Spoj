# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        q = [root]
        depth = {root.val: 0}
        x_par, y_par = None, None
        while q:
            current = q.pop(0)
            if current.left:
                q += [current.left]
                depth[current.left.val] = depth[current.val] + 1
                if current.left.val == x:
                    x_par = current.val
                if current.left.val == y:
                    y_par = current.val
            
            if current.right:
                q += [current.right]
                depth[current.right.val] = depth[current.val] + 1
                
                if current.right.val == x:
                    x_par = current.val
                if current.right.val == y:
                    y_par = current.val
            
        if depth[x] == depth[y] and x_par != y_par:
            return True
        else:
            return False
                