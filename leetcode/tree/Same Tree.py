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

        if i >= len(nums):
            break

        if nums[i]:
            node.right = TreeNode(nums[i])
            queue.append(node.right)

        i += 1

    return root

def get_node_value(node):
    if not node:
        return []

    left = get_node_value(node.left)
    right = get_node_value(node.right)
    return [node.val] + left + right

class Solution1:
    # DFS recursion
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

class Solution2:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue = collections.deque()
        queue.append((p, q))

        while queue:
            p_node, q_node = queue.pop()
            if not p_node and not q_node:
                continue
            if not p_node or not q_node:
                return False
            if p_node.val != q_node.val:
                return False

            queue.append((p_node.left, q_node.left))
            queue.append((p_node.right, q_node.right))
        return True


if __name__ == '__main__':
    p = create_binary_tree(nums = [1, 2])
    q = create_binary_tree(nums = [1, None, 2])
    so1 = Solution1()
    print(so1.isSameTree(p, q))
    so2 = Solution2()
    print(so2.isSameTree(p, q))
