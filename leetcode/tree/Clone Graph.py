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


class Solution:
    def cloneGraph(self, node: Node) -> Node:
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



if __name__ == '__main__':
    adjList = [[2, 4], [1, 3], [2, 4], [1, 3]]
    node = create_graph(adjList)
    so = Solution()
    print(so.cloneGraph(node).neighbors[0])
