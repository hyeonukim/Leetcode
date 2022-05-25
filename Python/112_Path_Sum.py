# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def answer(root, targetSum):
    if not root:
        return False
    
    if not root.left and not root.right and root.val == targetSum:
        return True
    
    targetSum -= root.val

    return answer(root.left, targetSum) or answer(root.right, targetSum)
    

if __name__ == "__main__":
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.right.right.right = TreeNode(1)

    print(answer(root, 22))