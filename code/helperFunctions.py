import networkx as nx
import easygui

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
def modularity(adj_matrix, node_communities):
    num_nodes = len(adj_matrix)

    # degree of each node (number of edges connected to it)
    degrees = []
    for i in range(num_nodes):
        degrees.append(sum(adj_matrix[i]))

    # total number of edges in the graph
    num_edges = sum(degrees) / 2

    modularity_score = 0

    for i in range(num_nodes):
        for j in range(num_nodes):
            if node_communities[i] == node_communities[j]:
                
                actual_edge = adj_matrix[i][j]
                expected_edge = (degrees[i] * degrees[j]) / (2 * num_edges)

                modularity_score += actual_edge - expected_edge

    return modularity_score / (2 * num_edges)

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

def showAsyncGUI():
    easygui.msgbox("Your algorithm is running. Please stand by...", "Community Detection Algorithm Comparisons")