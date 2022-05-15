# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def answer(root):
    curr, res, s = root, [], []
    while True:
        if curr:
            s.append(curr)
            curr = curr.left
        elif s:
            curr = s.pop()
            res.append(curr.val)
            curr = curr.right
        else:
            break
    return res
    
if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(5)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    res = answer(root)
    for x in res:
        print(x)