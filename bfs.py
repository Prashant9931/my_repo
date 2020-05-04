# from create_graph import Graph
#
#
# def BFS(graph, start):
#     queue = []
#     visited = [False] * len(graph)
#     queue.append(start)
#     visited[start] = True
#     while queue:
#         s = queue.pop(0)
#         print(s, end=" ")
#         for node in graph[s]:
#             if not visited[node]:
#                 queue.append(node)
#                 visited[node] = True
#
#
# graph_obj = Graph([(1, 0), (0, 2), (2, 1), (0, 3), (1, 4)], [0, 1, 2, 3, 4])
# starting_node = 2
# BFS(graph_obj, starting_node)
