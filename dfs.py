from create_graph import Graph


def dfs(graph, start):
    stack = []
    visited = [False] * len(graph)
    stack.append(start)
    while stack:
        s = stack[-1]
        stack.pop()
        if not visited[s]:
            print(s, end=' ')
            visited[s] = True
        for node in graph[s]:
            if not visited[node]:
                stack.append(node)


graph_obj = Graph([(1, 0), (0, 2), (2, 1), (0, 3), (1, 4)], [0, 1, 2, 3, 4])
starting_node=0
dfs(graph_obj, starting_node)
