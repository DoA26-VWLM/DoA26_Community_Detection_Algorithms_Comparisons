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
# node_communities is an array where the index is the node number and the value is the community
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

#Makes the community lists look better for output
def prettifyCommunities(communitiesArray: list[list]):
    #Each community string gets added to this list
    prettyArray = []
    prettyString = ""
    nodeCounter = 0
    communityCounter = 1
    while (communityCounter <= len(communitiesArray)):
        nodeCounter = 0
        prettyCommunityDisplay = "Community " + str(communityCounter) + ": "
        #Adds all the nodes to the string of a community
        while (nodeCounter < len(communitiesArray[communityCounter-1])):
            prettyCommunityDisplay = prettyCommunityDisplay + str(communitiesArray[communityCounter-1][nodeCounter])
            #Adds a comma if not the last element, and a new line if it is
            if (nodeCounter != (len(communitiesArray[communityCounter-1]) - 1)):
                prettyCommunityDisplay += ", "
            else:
                prettyCommunityDisplay += "\n"
            nodeCounter += 1
        prettyArray.append(prettyCommunityDisplay)
        communityCounter += 1
    
    for community in prettyArray:
        prettyString += community
    return prettyString

#Takes the output of an algorithm and converts it into a communities array for modularity scoring
def prepForMod(communitiesArray):
    communityValuesArray = []
    #Current Community
    communityNum = 0
    #Total number of nodes
    numNodes = 0
    currentNodeNum = 0
    #Counts the number of nodes to size the final array and gives the array default values
    for community in communitiesArray:
        for node in community:
            communityValuesArray.append(-1)
            numNodes += 1

    
    #Adds each node to its correct index(its node number) as the value of its community
    while communityNum < len(communitiesArray):
        currentNodeNum = 0
        while currentNodeNum < len(communitiesArray[communityNum]):
            communityValuesArray[int(communitiesArray[communityNum][currentNodeNum])] = communityNum
            currentNodeNum += 1
        communityNum += 1
    
    return communityValuesArray

    

    