from typing import Optional


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def create_binary_tree(nums):
    if not nums:
        return None

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


def get_tree_node_value(node):
    if node == None:
        return [None]

    else:
        left_value = get_tree_node_value(node.left)
        right_value = get_tree_node_value(node.right)
        return [node.val] + left_value + right_value


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def path_count(cur_node, target_sum, cur_path):
            if not cur_node:
                return 0

            cur_path.append(cur_node.val)
            path_sum = 0
            count_path = 0

            for i in range(len(cur_path) - 1, -1, -1):
                path_sum += cur_path[i]
                if path_sum == target_sum:
                    count_path += 1

            count_path += path_count(cur_node.left, target_sum, cur_path)
            count_path += path_count(cur_node.right, target_sum, cur_path)
            cur_path.pop()
            return count_path

        return path_count(root, targetSum, [])



if __name__ == '__main__':
    nums = [10, 5, -3, 3, 2, None, 11, 3, -2, None, 1]
    root = create_binary_tree(nums)
    so = Solution()
    print(so.pathSum(root, targetSum=8))

    # print(get_tree_node_value(root))
