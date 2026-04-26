import helperFunctions
import networkx as nx

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
def brute_force_community_detection(graph: nx.Graph):
    edges = helperFunctions.getEdges(graph)
    # get unique nodes
    nodes = []
    for (u, v) in edges:
        if u not in nodes:
            nodes.append(u)
        if v not in nodes:
            nodes.append(v)

    nodes.sort()

    # build adjacency matrix
    A, index = helperFunctions.build_adj_matrix(edges, nodes)

    best_partition = None
    best_score = -999999 # Base score to start comparison.

    # generate all partitions recursivley
    partitions = generate_partitions(len(nodes))

    # test each partition and score them, the loop outputs the best scoring
    for partition in partitions:
        score = helperFunctions.modularity(A, partition)

        if score > best_score:
            best_score = score
            best_partition = partition

    # convert to grouped output for formatting for the purposes of testing and figuring out what we are doing
    grouped = group_communities(nodes, best_partition)

    communities = list(grouped.values())

    return communities, best_score