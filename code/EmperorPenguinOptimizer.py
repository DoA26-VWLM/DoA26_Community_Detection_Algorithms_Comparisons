import random
import networkx as nx
import math


# -------------------------
# INITIAL POPULATION
# -------------------------
def initialize_penguin_population(graph, num_penguins):
    """
    Each penguin = a candidate community assignment:
        {node: community_id}
    """
    population = []
    nodes = list(graph.nodes())
    num_nodes = len(nodes)

    for _ in range(num_penguins):
        assignment = {}

        for node in nodes:
            # Random community assignment initially
            assignment[node] = random.randint(0, num_nodes - 1)

        population.append(assignment)

    return population


# -------------------------
# CONVERT ASSIGNMENT -> COMMUNITIES
# -------------------------
def build_communities_from_assignment(assignment):
    """
    Converts:
        {node: community_id}
    into:
        [set(nodes_in_community), ...]
    """
    communities = {}

    for node, community_id in assignment.items():
        if community_id not in communities:
            communities[community_id] = set()
        communities[community_id].add(node)

    return list(communities.values())


# -------------------------
# MANUAL MODULARITY FUNCTION
# -------------------------
def compute_modularity(graph, assignment):
    """
    Manual implementation of modularity:

    Q = sum over communities:
        (in_degree / 2m) - (total_degree / 2m)^2
    """

    communities = build_communities_from_assignment(assignment)

    num_edges = graph.number_of_edges()
    if num_edges == 0:
        return 0

    two_m = 2 * num_edges
    modularity_score = 0.0

    for community in communities:
        internal_edge_count = 0
        total_degree = 0

        for node in community:
            total_degree += graph.degree[node]

            for neighbor in graph.neighbors(node):
                if neighbor in community:
                    internal_edge_count += 1

        # Each edge counted twice in undirected graphs
        internal_edge_count /= 2

        modularity_score += (internal_edge_count / two_m) - (total_degree / two_m) ** 2

    return modularity_score


# -------------------------
# TEMPERATURE SCHEDULING (STEP 5)
# -------------------------
def compute_behavior_probabilities(current_iteration, max_iterations, cooling_rate=0.95):
    """
    Controls exploration vs exploitation.

    Early iterations → more randomness
    Late iterations → more convergence
    """

    temperature = cooling_rate ** current_iteration

    exploration_probability = temperature
    exploitation_probability = 1 - temperature

    probability_copy_best = exploitation_probability * 0.7
    probability_follow_neighbors = exploitation_probability * 0.3
    probability_random_change = exploration_probability

    return (
        probability_copy_best,
        probability_follow_neighbors,
        probability_random_change
    )


# -------------------------
# LOCAL STRUCTURE HELPER
# -------------------------
def get_most_common_neighbor_community(graph, node, assignment):
    """
    Looks at neighbors and returns the most common community label.
    """

    neighbor_nodes = list(graph.neighbors(node))

    if not neighbor_nodes:
        return assignment[node]

    community_frequency = {}

    for neighbor in neighbor_nodes:
        neighbor_community = assignment[neighbor]
        community_frequency[neighbor_community] = community_frequency.get(neighbor_community, 0) + 1

    return max(community_frequency, key=community_frequency.get)


# -------------------------
# MAIN EPO ALGORITHM
# -------------------------
def emperor_penguin_optimization_community_detection(graph: nx.Graph):
    """
    Main optimization loop.
    """
    finalCommunities = []
    communityNum: int = 0
    numEmpty = 0

    #Determine number penguins
    edgesNum = len(graph.edges)
    nodesNum = len(graph.nodes)
    base = math.sqrt(nodesNum)
    density = (2 * edgesNum) / (nodesNum * (nodesNum - 1))
    densityFactor = 1.0 + (0.5 * (1-density))
    population_size = base * densityFactor
    minPop = 5
    maxPop = 200
    population_size = int(min(maxPop, max(minPop, population_size)))
    population = initialize_penguin_population(graph, population_size)

    #Determine number of iterations
    max_iterations = math.ceil((len(population) * nodesNum) * density)

    best_assignment_overall = None
    best_modularity_score = float("-inf")

    nodes = list(graph.nodes())

    for iteration in range(max_iterations):

        # -------------------------
        # Evaluate population
        # -------------------------
        fitness_scores = []

        for assignment in population:
            score = compute_modularity(graph, assignment)
            fitness_scores.append(score)

            if score > best_modularity_score:
                best_modularity_score = score
                best_assignment_overall = assignment.copy()

        # -------------------------
        # Compute temperature-based behavior
        # -------------------------
        p_copy_best, p_neighbor, p_random = compute_behavior_probabilities(
            iteration, max_iterations
        )

        # -------------------------
        # Update population
        # -------------------------
        new_population = []

        for assignment in population:
            updated_assignment = assignment.copy()

            for node in nodes:
                rand_value = random.random()

                # 1. Copy from best solution
                if rand_value < p_copy_best:
                    updated_assignment[node] = best_assignment_overall[node]

                # 2. Follow neighbor structure
                elif rand_value < p_copy_best + p_neighbor:
                    updated_assignment[node] = get_most_common_neighbor_community(
                        graph, node, assignment
                    )

                # 3. Random exploration
                else:
                    updated_assignment[node] = random.randint(0, len(nodes) - 1)

            new_population.append(updated_assignment)

        population = new_population

    #Reformats the data to our standardized format
    while (numEmpty < len(best_assignment_overall)):
        communityArray = []
        numEmpty = 0
        for node in best_assignment_overall:
            if best_assignment_overall[node] == communityNum:
                communityArray.append(node)
                best_assignment_overall[node] = -1
            elif best_assignment_overall[node] == -1:
                numEmpty += 1
        if (len(communityArray) > 0):
            finalCommunities.append(communityArray)
        communityNum += 1
            
    print(finalCommunities)
    return finalCommunities