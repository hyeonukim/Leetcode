class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def answer(nums):
    if not nums:
        return None
    mid = len(nums)//2

    root = TreeNode(nums[mid])
    root.left = answer(nums[:mid])
    root.right = answer(nums[mid+1:])

    return root
if __name__ == "__main__":
    arr = [-10,3,0,5,9]
    root = answer(arr)
    print(root.val)