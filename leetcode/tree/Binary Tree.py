class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def create_binary_tree(nums):
    if nums is None:
        return None

    root = TreeNode(nums[0])

    queue = [root]

    i = 1
    while i < len(nums):
        node = queue.pop(0)

        if nums[i] is not None:
            node.left = TreeNode(nums[i])
            queue.append(node.left)

        i += 1

        if nums[i] is not None and i < len(nums):
            node.right = TreeNode(nums[i])
            queue.append(node.right)

        i += 1

    return root


if __name__ == '__main__':
    nums = [1, 2, 3, 4, None, 5, 6, None, None, 7, None]
    root = create_binary_tree(nums)
    print(root.left.val)
