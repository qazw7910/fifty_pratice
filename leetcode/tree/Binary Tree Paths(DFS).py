from typing import Optional, List


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

        if nums[i] != None:
            node.left = TreeNode(nums[i])
            queue.append(node.left)

        i += 1

        if nums[i] != None and i < len(nums):
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
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def find_path(cur_node, cur_path, all_paths):
            if not cur_node:
                return

            cur_path.append(str(cur_node.val))

            if not cur_node.left and not cur_node.right:
                all_paths.append("->".join(cur_path))

            find_path(cur_node.left, cur_path, all_paths)
            find_path(cur_node.right, cur_path, all_paths)
            cur_path.pop()

        all_paths = []
        find_path(root, [], all_paths)
        return all_paths


if __name__ == '__main__':
    nums = [1, 2, 3, None, 5]
    root = create_binary_tree(nums)
    so = Solution()
    print(get_tree_node_value(root))
    print(so.binaryTreePaths(root=root))
