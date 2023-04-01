def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    so = Solution()
    result = so.diameterOfBinaryTree(root)
    print(result)


class TreeNode:
    def __init__(self, root=0, left=None, right=None):
        self.root = root
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.diameter = 0

        def max_depth(node):
            if node is None:
                return 0

            left_depth = max_depth(node.left)
            right_depth = max_depth(node.right)

            self.diameter = max(self.diameter, left_depth + right_depth)

            return 1 + max(left_depth, right_depth)

        max_depth(root)

        return self.diameter


if __name__ == '__main__':
    main()
