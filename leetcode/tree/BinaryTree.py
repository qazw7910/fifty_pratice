def main():
    nums = [1, 2, 3, 4, None, 5, 6, None, None, 7, None]
    root = createBinaryTree(nums)
    print(root.left.val)


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def createBinaryTree(nums):
    if not nums:
        return None

    # create the root node
    root = TreeNode(nums[0])

    # initialize a queue with the root node
    queue = [root]

    i = 1
    while i < len(nums):
        # get the next node from the queue
        node = queue.pop(0)

        # create the left child node if it exists
        if nums[i] is not None:
            node.left = TreeNode(nums[i])
            queue.append(node.left)
        i += 1

        # create the right child node if it exists
        if nums[i] is not None and i < len(nums):
            node.right = TreeNode(nums[i])
            queue.append(node.right)
        i += 1

    return root


if __name__ == '__main__':
    main()
