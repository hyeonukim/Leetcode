# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def getHeight(root):
    if not root:
        return 0

    return 1+max(getHeight(root.left), getHeight(root.right))

def answer(root):
    if not root:
        return True
    
    return abs(getHeight(root.left)-getHeight(root.right)) < 2 and answer(root.left) and answer(root.right)


    return
if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    root.right.right.right = TreeNode(10)

    print(answer(root))