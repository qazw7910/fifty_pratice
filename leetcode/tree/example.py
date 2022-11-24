def main():
    sampleTree = treeNode(5)
    sampleTree.insertRight(7)
    sampleTree.insertRight(8)
    sampleTree.insertLeft(3)
    sampleTree.insertLeft(2)
    sampleTree.right.insertLeft(6)
    sampleTree.right.right.insertRight(3)
    sampleTree.right.right.right.insertRight(3)
    sampleTree.left.insertRight(4)


class treeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insertLeft(self, value):
        if self.left is None:
            self.left = treeNode(value)
        else:
            self.left.insertLeft(value)

    def insertRight(self, value):
        if self.right is None:
            self.right = treeNode(value)
        else:
            self.right.insertRight(value)


if __name__ == '__main__':
    main()
