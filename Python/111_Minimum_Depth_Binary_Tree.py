# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def answer(root):
    if not root:
        return 0
    
    if None in [root.left, root.right]:
        return max(answer(root.left), answer(root.right))+1
    else:
        return min(answer(root.left), answer(root.right))+1

if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    print(answer(root))