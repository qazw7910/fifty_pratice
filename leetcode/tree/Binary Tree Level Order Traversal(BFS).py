import collections
from typing import Optional, List


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

        if nums[i]:
            node.right = TreeNode(nums[i])
            queue.append(node.right)
        i += 1
    return root


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = collections.deque()
        queue.append(root)
        result = []

        while queue:
            cur_level_size = len(queue)
            cur_level_list = []

            for _ in range(cur_level_size):
                node = queue.popleft()
                cur_level_list.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            result.append(cur_level_list)

        return result


if __name__ == '__main__':
    nums = [3, 9, 20, None, None, 15, 7]
    root = create_binary_tree(nums)
    so = Solution()
    print(so.levelOrder(root))
