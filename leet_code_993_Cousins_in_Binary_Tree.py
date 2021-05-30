# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        q = [root]
        visited = []
        lvl = {root.val:0}
        x_par,y_par = None, None
        while q:
            temp = q.pop(0)
            if temp.val in visited:
                continue
            visited += [temp.val]
            
            if temp.left:
                q += [temp.left]
                lvl[temp.left.val] = lvl[temp.val] +1
                if temp.left.val == x:
                    x_par = temp.val
                if temp.left.val == y:
                    y_par = temp.val
                    
            if temp.right:
                q += [temp.right]
                lvl[temp.right.val] = lvl[temp.val] +1


                if temp.right.val == x:
                    x_par = temp.val
                if temp.right.val == y:
                    y_par = temp.val
        print("x_par= ",x_par)
        print("y_par=", y_par)
        print(lvl)
        
        if lvl[x] == lvl[y] and x_par != y_par:
            return True
        else:
            return False