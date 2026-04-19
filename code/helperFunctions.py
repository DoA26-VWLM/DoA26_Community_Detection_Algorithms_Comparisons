import networkx as nx

def build_adj_matrix(edges, nodes):
    n = len(nodes)

    # map node -> index
    index = {}
    for i in range(n):
        index[nodes[i]] = i

    # create empty matrix
    A = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(0)
        A.append(row)

    # fill edges (undirected)
    for (u, v) in edges:
        i = index[u]
        j = index[v]
        A[i][j] = 1
        A[j][i] = 1

    return A, index


# Compute modularity
# What this does is scores each partition based on how many edges are within communities vs between communities.
def modularity(A, communities):
    n = len(A)

    # degree of each node
    k = []
    for i in range(n):
        k.append(sum(A[i]))

    # total number of edges
    m = sum(k) / 2

    Q = 0
    for i in range(n):
        for j in range(n):
            if communities[i] == communities[j]:
                Q += A[i][j] - (k[i] * k[j]) / (2 * m)

    return Q / (2 * m)

# Retrieves edges from graph as a normal array
def getEdges(graph: nx.Graph):
    edgeArray = []
    for edge in graph.edges:
        edgeArray.append(edge)
    return edgeArray

#Retrieves vertices from graph as a normal array
def getVertices(graph: nx.Graph):
    verticesArray = []
    for vertex in graph.nodes:
        verticesArray.append(vertex)
    return verticesArray