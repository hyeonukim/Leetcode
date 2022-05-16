# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def answer(self,p,q):
        if p and q:
            return p.val == q.val and self.answer(p.left, q.left) and self.answer(p.right, q.right)
        else:
            return p == q

        
if __name__ == "__main__":
    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(3)

    q = TreeNode(1)
    q.left = TreeNode(2)

    sol = Solution()
    print(sol.answer(p,q))