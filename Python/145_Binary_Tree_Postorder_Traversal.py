# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def answer(root):
    res, stack = [], [root]
    while stack:
        curr = stack.pop()
        if curr:
            res.append(curr.val)
            stack.append(curr.left)
            stack.append(curr.right)
    return res[::-1]

if __name__ == "__main__":
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)

    print(answer(root))