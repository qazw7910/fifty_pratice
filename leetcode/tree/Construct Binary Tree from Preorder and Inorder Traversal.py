import collections
from typing import List, Optional

from pip._internal.cli.cmdoptions import pre


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def create_binary_tree(nums):
    root = TreeNode(nums[0])
    queue = collections.deque()
    queue.append(root)

    i = 1
    while i < len(nums):
        node = queue.popleft()

        if nums[i]:
            node.left = TreeNode(nums[i])
            queue.append(node.left)
        i += 1

        if i >= len(nums):
            break

        if nums[i]:
            node.right = TreeNode(nums[i])
            queue.append(node.right)
        i += 1

    return root


def get_tree_node_BFS(root: Optional[TreeNode]):
    if not root:
        return []

    result = [root.val]
    queue = collections.deque()
    queue.append(root)

    while queue:
        node = queue.popleft()

        if node.left:
            result.append(node.left.val)
            queue.append(node.left)
        else:
            result.append(None)

        if node.right:
            result.append(node.right.val)
            queue.append(node.right)
        else:
            result.append(None)
    return result


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preorder_queue = collections.deque(preorder)
        inorder_len = len(inorder) - 1
        inorder_lookup = {}

        for idx, value in enumerate(inorder):
            inorder_lookup[value] = idx

        def buildTree(left, right):
            if left > right:
                return

            node = preorder_queue.popleft()
            mid = inorder_lookup[node]
            root = TreeNode(node)
            root.left = buildTree(left, mid - 1)
            root.right = buildTree(mid + 1, right)
            return root

        return buildTree(0, inorder_len)


if __name__ == '__main__':
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    so = Solution()
    root = so.buildTree(preorder, inorder)
    print(get_tree_node_BFS(root))
