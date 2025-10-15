print("------------Question no 1------------------")

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

def dfs(graph, start):
    visited, stack, path = set(), [start], []

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            path.append(node)
            stack.extend(reversed(graph[node]))

    return path

a = dfs(graph, 'A')
print("DFS Path: ", a)

