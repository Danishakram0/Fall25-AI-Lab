print("------------Question no 1------------------")

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
def bfs(graph, start_point):
    visited_nodes = set()
    queue = [start_point]
    path_order = []

    for i in range(len(graph)):
        if not queue:
            break

        current = queue.pop(0)
        if current not in visited_nodes:
            visited_nodes.add(current)
            path_order.append(current)

            for next_node in graph[current]:
                if next_node not in visited_nodes:
                    queue.append(next_node)

    return path_order

a = bfs(graph, 'A')
print("BFS Path: ", a)
