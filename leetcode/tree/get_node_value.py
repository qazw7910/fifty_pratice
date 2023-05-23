import collections


def main():
    pass
def get_node_value_BFS(tree):
    if not tree:
        return []

    result = []
    result.append(tree.val)

    queue = collections.deque()
    queue.append(tree)
    while queue:
        node = queue.popleft()
        if node.left:
            result.append(node.left.val)
            queue.append(node.left)

        if node.right:
            result.append(node.right.val)
            queue.append(node.right)
    return result

def get_node_value_DFS(node):
    if not node:
        return []

    left = get_node_value_DFS(node.left)
    right = get_node_value_DFS(node.right)
    return [node.val] + left + right

if __name__ == '__main__':
    main()