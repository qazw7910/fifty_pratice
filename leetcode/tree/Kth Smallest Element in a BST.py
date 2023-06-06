import collections
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def create_binary_tree(nums: List[int]) -> TreeNode:
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

        if nums[i]:
            node.right = TreeNode(nums[i])
            queue.append(node.right)
        i += 1
    return root


def get_node_value_BFS(root):
    if not root:
        return None

    queue = collections.deque()
    queue.append(root)
    result = [root.val]

    while queue:
        node = queue.popleft()

        if node.left:
            result.append(root.left.val)
            queue.append(node.left)
        else:
            result.append(None)

        if node.right:
            result.append(root.right.val)
            queue.append(node.right)
        else:
            result.append(None)

    return result


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        stack.append(root)

        while stack:
            while root:
                stack.append(root)
                root = root.left

            node = stack.pop()
            k -= 1

            if k == 0:
                return node.val

            root = node.right


if __name__ == "__main__":
    nums = [5, 3, 6, 2, 4, None, None, 1]
    root = create_binary_tree(nums)
    k = 4
    so = Solution()
    print(get_node_value_BFS(root))
    print(so.kthSmallest(root, k))
