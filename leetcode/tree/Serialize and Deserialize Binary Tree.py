import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def create_binary_tree(nums):
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

def get_node_value_BFS(tree):
    if not tree:
        return

    result = [tree.val]
    queue = collections.deque()
    queue.append(tree)

    while queue:
        node = queue.popleft()

        if node.left:
            result.append(node.left.val)
            queue.append(node.left)
        else:
            result.append('None')


        if node.right:
            result.append(node.right.val)
            queue.append(node.right)
        else:
            result.append('None')
    return result


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        result = []

        def preorder(node):
            if not node:
                result.append("None")
                return
            result.append(str(node.val))
            preorder(node.left)
            preorder(node.right)

        # ['1', '2', 'None', 'None', '3', '4', 'None', 'None', '5', 'None', 'None']
        preorder(root)
        return " ".join(result)  # '1 2 None None 3 4 None None 5 None None'

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        # '1 2 None None 3 4 None None 5 None None'
        data_list = data.split(" ")
        queue = collections.deque(data_list)

        def deserialize_helper(queue):
            node = queue.popleft()
            if node == "None":
                return
            root = TreeNode(node)
            root.left = deserialize_helper(queue)
            root.right = deserialize_helper(queue)
            return root

        return deserialize_helper(queue)

if __name__ == '__main__':
    nums = [1, 2, 3, None, None, 4, 5]
    root = create_binary_tree(nums)
    so = Codec()
    serialize_data = so.serialize(root)
    print(serialize_data)
    deserialize_data = so.deserialize(serialize_data)
    print(get_node_value_BFS(deserialize_data))
