from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def create_binary_tree(nums):
    root = TreeNode(nums[0])

    queue = [root]

    i = 1

    while i < len(nums):

        node = queue.pop()

        if nums[i] != None:
            node.left = TreeNode(nums[i])
            queue.append(node.left)

        i += 1

        if nums[i] != None and i < len(nums):
            node.right = TreeNode(nums[i])
            queue.append(node.right)

        i += 1

    return root


def get_node_value(node):
    if not node:
        return [None]
    else:
        left = get_node_value(node.left)
        right = get_node_value(node.right)

        return [node.val] + left + right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        def find_diameter(node):
            if not node:
                return 0

            left = find_diameter(node.left)
            right = find_diameter(node.right)

            self.diameter = max(self.diameter, left + right)

            return 1 + max(left, right)

        find_diameter(root)

        return self.diameter


if __name__ == '__main__':
    root = create_binary_tree(nums=[1, 2, 3, 4, 5])
    so = Solution()
    print(so.diameterOfBinaryTree(root))
