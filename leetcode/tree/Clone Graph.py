import collections


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors else []


def create_graph(adjList) -> Node:
    nodes = {}

    for i in range(len(adjList)):
        nodes[i + 1] = Node(i + 1, [])

    for i in range(len(adjList)):
        for neighbor in adjList[i]:
            nodes[i + 1].neighbors.append(nodes[neighbor])

    return nodes[1] if nodes else None


class Solution1:
    def cloneGraph(self, node: Node) -> Node:
        if not node:
            return node
        # Node.val:           1       2       3       4
        # Node.neighbors: [[2, 4], [1, 3], [2, 4], [1, 3]]
        visited = {}
        queue = collections.deque()
        queue.append(node)
        visited[node] = Node(node.val, [])

        while queue:
            visited_node = queue.popleft()
            for neighbor in visited_node.neighbors:
                if neighbor not in visited:
                    visited[neighbor] = Node(neighbor.val, [])
                    queue.append(visited[neighbor])
                visited[visited_node].neighbors.append(visited[neighbor])
        return visited[node]

class Solution2:
    def cloneGraph(self, node: 'Node') -> 'Node':
        root = node
        if node is None:
            return node

        # traverse, get all nodes by BFS
        old_nodes = self.get_all_nodes(node)
        # print(len(nodes))

        # clone all nodes
        mapping = {}
        for old_node in old_nodes:
            mapping[old_node] = Node(old_node.val)

        # clone all edges
        for old_node in old_nodes: #
            new_node = mapping[old_node]
            for neighbor in old_node.neighbors:
                new_neighbor = mapping[neighbor]
                new_node.neighbors.append(new_neighbor)

        return mapping[root]


    def get_all_nodes(self, node):
        queue = [node]
        result = set([node])
        while queue:
            head = queue.pop(0)
            for neighbor in head.neighbors:
                if neighbor not in result:
                    result.add(neighbor)
                    queue.append(neighbor)

        return result




if __name__ == '__main__':
    adjList = [[2, 4], [1, 3], [2, 4], [1, 3]]
    node = create_graph(adjList)
    so = Solution2()
    print(so.cloneGraph(node).neighbors[0].neighbors[0].val)
