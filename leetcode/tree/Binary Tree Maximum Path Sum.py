from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def create_binary_tree(nums):
    if not nums:
        return None

    root = TreeNode(nums[0])

    queue = [root]

    i = 1

    while i < len(nums):

        node = queue.pop(0)

        if nums[i]:
            node.left = TreeNode(nums[i])
            queue.append(node.left)

        i += 1

        if nums[i] and i < len(nums):
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
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def find_max_path_sum(node):
            if not node:
                return 0
            # Postorder: Left, Rright, Node
            left = max(find_max_path_sum(node.left), 0)
            right = max(find_max_path_sum(node.right), 0)
            cur_path_sum = node.val + left + right

            self.max_path_sum = max(self.max_path_sum, cur_path_sum)

            return node.val + max(left, right)

        self.max_path_sum = float("-inf")
        find_max_path_sum(root)

        return self.max_path_sum


if __name__ == '__main__':
    nums = [-10, 9, 20, None, None, 15, 7]
    root = create_binary_tree(nums)
    so = Solution()
    print(so.maxPathSum(root))
