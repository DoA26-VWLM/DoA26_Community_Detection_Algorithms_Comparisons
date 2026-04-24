import random
import networkx as nx


def label_propagation(graph, max_iter=100):
    """
    Perform community detection using the Label Propagation algorithm.

    Parameters:
        graph (networkx.Graph): Input graph (unweighted, undirected assumed)
        max_iter (int): Maximum number of iterations to prevent infinite loops

    Returns:
        List[List[node]]: A list of communities, where each community is a list of nodes
    """

    # Step 1: Initialize labels
    # Each node starts with a unique label (its own ID)
    node_labels = {node: node for node in graph.nodes()}

    # Step 2: Iteratively update labels
    for iteration in range(max_iter):
        labels_changed = False  # Track if any label changes this iteration

        # Shuffle node order for asynchronous updates
        nodes = list(graph.nodes())
        random.shuffle(nodes)

        # Step 3: Visit each node and update its label
        for current_node in nodes:

            # Get neighbors of the current node
            neighbor_nodes = list(graph.neighbors(current_node))

            # Skip isolated nodes
            if not neighbor_nodes:
                continue


            # Step 4: Count neighbor labels

            neighbor_label_counts = {}

            for neighbor in neighbor_nodes:
                neighbor_label = node_labels[neighbor]

                if neighbor_label not in neighbor_label_counts:
                    neighbor_label_counts[neighbor_label] = 0
                neighbor_label_counts[neighbor_label] += 1


            # Step 5: Find most frequent label(s)

            max_frequency = max(neighbor_label_counts.values())

            most_frequent_labels = []
            for label, count in neighbor_label_counts.items():
                if count == max_frequency:
                    most_frequent_labels.append(label)


            # Step 6: Random tie-breaking

            selected_label = random.choice(most_frequent_labels)


            # Step 7: Update label if changed

            if node_labels[current_node] != selected_label:
                node_labels[current_node] = selected_label
                labels_changed = True

        # Step 8: Stop if no changes occurred
        if not labels_changed:
            break

    # Step 9: Group nodes into communities
    communities_by_label = {}

    for node, label in node_labels.items():
        if label not in communities_by_label:
            communities_by_label[label] = []
        communities_by_label[label].append(node)

    return list(communities_by_label.values())