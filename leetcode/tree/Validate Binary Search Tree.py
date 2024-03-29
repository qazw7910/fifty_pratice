import collections
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def create_binary_tree(nums):
    if not nums:
        return

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

        if nums[i] and i < len(nums):
            node.right = TreeNode(nums[i])
            queue.append(node.right)
        i += 1

    return root


def get_node_value_BFS(tree):
    if not tree:
        return []

    result = [tree.val]
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


class Solution1:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # DFS
        def is_valid(node, smallest, biggest):
            if not node:
                return True

            if node.val <= smallest or node.val >= biggest:
                return False

            return is_valid(node.left, smallest, node.val) and is_valid(node.right, node.val, biggest)

        return is_valid(root, float("-inf"), float("inf"))

        # ----------------------------------------------------------------


class Solution2:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # BFS
        if not root:
            return True

        stack = [(root, float("-inf"), float("inf"))]

        while stack:
            node, smallest, biggest = stack.pop()

            if not node:
                continue

            if node.val <= smallest or node.val >= biggest:
                return False

            stack.append((node.left, smallest, node.val))
            stack.append((node.right, node.val, biggest))

        return True


if __name__ == '__main__':
    nums = [2, 1, 3]
    root = create_binary_tree(nums)
    # print(get_node_value_BFS(root))
    so = Solution2()
    print(so.isValidBST(root))
