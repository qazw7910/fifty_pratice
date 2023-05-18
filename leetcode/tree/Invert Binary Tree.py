import collections
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


def get_node_value_DFS(node):
    if not node:
        return []

    left = get_node_value_DFS(node.left)
    right = get_node_value_DFS(node.right)
    return [node.val] + left + right


def get_node_value_BFS(tree):
    if not tree:
        return []

    result = []
    result.append(tree.val)

    queue = collections.deque()
    queue.append(tree)
    while queue:
        node = queue.popleft()
        if node.left:
            result.append(node.left.val)
            queue.append(node.left)

        if node.right:
            result.append(node.right.val)
            queue.append(node.right)
    return result


class Solution:
    def invertTree(self, root: Optional[TreeNode]):
        # BFS
        # if not root:
        #     return
        #
        # queue = collections.deque()
        # queue.append(root)
        #
        # while queue:
        #     node = queue.popleft()
        #     node.left, node.right = node.right, node.left
        #
        #     if node.left:
        #         queue.append(node.left)
        #     if node.right:
        #         queue.append(node.right)
        #
        # return root
        # ----------------------------------------------------------------
        # DFS
        # preorder: node left right
        if not root:
            return

        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root


if __name__ == '__main__':
    nums = [4, 2, 7, 1, 3, 6, 9]
    root = create_binary_tree(nums)
    print(get_node_value_BFS(root))
    so = Solution()
    root = so.invertTree(root)
    print(get_node_value_BFS(root))
