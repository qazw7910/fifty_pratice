import collections
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def create_binary_tree(nums:List[int]):
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
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def is_same_tree(tree1: Optional[TreeNode], tree2: Optional[TreeNode]):
            if not tree1 and not tree2:
                return True
            if not tree1 or not tree2:
                return False
            if tree1.val != tree2.val:
                return False

            return is_same_tree(tree1.left, tree2.left) and is_same_tree(tree1.right, tree2.right)

        if not root and not subRoot:
            return True
        if root and not subRoot:
            return True
        if not root and subRoot:
            return False

        return is_same_tree(root, subRoot) or \
               self.isSubtree(root.left, subRoot) or \
               self.isSubtree(root.right, subRoot)


if __name__ == '__main__':
    root = create_binary_tree([3,4,5,1,2])
    subRoot = create_binary_tree([4,1,2])
    so = Solution()
    print(so.isSubtree(root, subRoot))