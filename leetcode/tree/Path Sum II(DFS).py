from typing import Optional, List


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
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def find_path(cur_node, target_sum, cur_path, all_paths):
            if not cur_node:
                return

            cur_path.append(cur_node.val)

            if cur_node.val == target_sum and not cur_node.left and not cur_node.right:
                all_paths.append(list(cur_path))

            else:
                find_path(cur_node.left, target_sum - cur_node.val, cur_path, all_paths)
                find_path(cur_node.right, target_sum - cur_node.val, cur_path, all_paths)
            cur_path.pop()
        all_paths = []
        find_path(root, targetSum, [], all_paths)
        return all_paths


if __name__ == '__main__':
    nums = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]
    root = create_binary_tree(nums)
    so = Solution()
    # print(get_tree_node_value(root))
    print(so.pathSum(root=root, targetSum=22))
