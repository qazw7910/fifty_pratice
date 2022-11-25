def main():
    root = TreeNode(1)
    root.insertLeft(2)
    root.insertRight(3)
    root.left.insertLeft(4)
    root.left.insertRight(5)

    so = Solution()
    print(so.diameterOfBinaryTree(root))


class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


    def insertLeft(self, value):
        if self.left is None:
            self.left = TreeNode(value)
        else:
            self.left.insertLeft(value)

    def insertRight(self, value):
        if self.right is None:
            self.right = TreeNode(value)
        else:
            self.right.insertRight(value)



class Solution:
    def diameterOfBinaryTree(self, root) -> int:
        self.ans = 0

        def depth(p):
            if not p:
                return 0
            left = depth(p.left)
            right = depth(p.right)
            self.ans = max(self.ans, left + right)
            return 1 + max(left, right)

        depth(root)
        return self.ans

if __name__ == '__main__':
    main()
