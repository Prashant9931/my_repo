def make_graph_(vertex_list):
    graph = {}
    for i in vertex_list:
        graph[i] = []
    return graph


def addEdge(edge,graph):
    graph[edge[0]].append(edge[1])


def Graph(set_of_edges, lst_of_vertics):
    graph=make_graph_(lst_of_vertics)
    for edge in set_of_edges:
        addEdge(edge,graph)
    return graph
