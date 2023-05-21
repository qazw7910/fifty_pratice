import collections
from typing import Optional


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


class Solution1:
    # BFS
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = collections.deque()
        queue.append((root, 1))
        maxlevel = 0

        while queue:
            node, level = queue.popleft()

            maxlevel = max(maxlevel, level)

            if node.left:
                queue.append((node.left, level + 1))

            if node.right:
                queue.append((node.right, level + 1))

        return maxlevel


class Solution2:
    # DFS
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


if __name__ == '__main__':
    nums = [3, 9, 20, None, None, 15, 7]
    root = create_binary_tree(nums)
    so = Solution2()
    print(so.maxDepth(root))
