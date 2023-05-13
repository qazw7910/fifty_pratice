from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def create_binary_tree(nums):
    if nums is None:
        return None

    root = TreeNode(nums[0])

    queue = [root]

    i = 1
    while i < len(nums):
        node = queue.pop(0)

        if nums[i] is not None:
            node.left = TreeNode(nums[i])
            queue.append(node.left)

        i += 1

        if nums[i] is not None and i < len(nums):
            node.right = TreeNode(nums[i])
            queue.append(node.right)

        i += 1

    return root


def get_tree_node_value(node):
    if node is None:
        return [None]

    else:
        left_value = get_tree_node_value(node.left)
        right_value = get_tree_node_value(node.right)
        return [node.val] + left_value + right_value

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # edge case
        if not root: # root == None : return False
            return False
        # base case
        if targetSum == root.val and not root.left and not root.right:
            return True

        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)



if __name__ == '__main__':
    nums = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]
    root = create_binary_tree(nums)
    so = Solution()
    # print(get_tree_node_value(root))
    print(so.hasPathSum(root = root, targetSum = 22))
