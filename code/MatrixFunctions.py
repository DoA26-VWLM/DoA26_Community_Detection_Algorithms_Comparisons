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