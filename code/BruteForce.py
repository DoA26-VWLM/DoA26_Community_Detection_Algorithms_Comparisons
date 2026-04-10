# Build adjacency matrix from edge list
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



# Generate ALL partitions (brute force)
def generate_partitions(n):
    partitions = []

    # NOTE: Used AI and an online example to help explain this spagetti of a recursive function
    
    def helper(i, current, max_label): # Recursive communitty permutation generator
        if i == n:
            partitions.append(current[:])
            return

        # Recursivley tries assigning to existing communities, and all subsequent combinations
        for label in range(max_label + 1):
            current[i] = label
            helper(i + 1, current, max_label)

        # create new community
        current[i] = max_label + 1
        helper(i + 1, current, max_label + 1)

    helper(0, [0] * n, 0)
    return partitions

# Convert node-community into grouped form
def group_communities(nodes, partition):
    groups = {}

    for i in range(len(nodes)):
        node = nodes[i]
        comm = partition[i]

        if comm not in groups:
            groups[comm] = []

        groups[comm].append(node)

    return groups



# Main brute force algorithm
def brute_force_community_detection(edges):
    # get unique nodes
    nodes = []
    for (u, v) in edges:
        if u not in nodes:
            nodes.append(u)
        if v not in nodes:
            nodes.append(v)

    nodes.sort()

    # build adjacency matrix
    A, index = build_adj_matrix(edges, nodes)

    best_partition = None
    best_score = -999999 # Base score to start comparison.

    # generate all partitions recursivley
    partitions = generate_partitions(len(nodes))

    # test each partition and score them, the loop outputs the best scoring
    for partition in partitions:
        score = modularity(A, partition)

        if score > best_score:
            best_score = score
            best_partition = partition

    # convert to grouped output for formatting for the purposes of testing and figuring out what we are doing
    grouped = group_communities(nodes, best_partition)

    return grouped, best_score


# HARD CODED EXAMPLE FOR TESTING

if __name__ == "__main__": # THIS IS FORMATTED AS:
    edges = [
        (0, 1), # 0 is adjacent to 1
        (0, 2), # 0 is adjacent to 2
        (1, 2), # 1 is adjacent to 2
        (3, 4) # 3 is adjacent to 4
    ]

    communities, score = brute_force_community_detection(edges)

    print("Best community grouping:")
    print(communities)
    print("Modularity score:", score)