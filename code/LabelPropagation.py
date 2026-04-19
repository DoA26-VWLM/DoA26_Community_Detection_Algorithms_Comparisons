import networkx as nx
import helperFunctions
import random

#This only works on a 0 based graph (first vertex is 0). If that isn't there, just add a 0 node that connects to nothing. 
# This functions does label propagation. The labels parameter indicates how many unique labels should be used
def labelPropagation(graph: nx.Graph, numLabels: int):
    nodes = helperFunctions.getVertices(graph)
    nodeLabels = []
    adjacencyLists = nx.to_dict_of_lists(graph)
    stable = 0
    nodeLabelOptions = [0] * numLabels
    numPasses = 0
    communitiesArray = []
    newLabelsArray = [0] * len(nodes)

    print(adjacencyLists)
    print(nodes) #debugging
    print(nodeLabelOptions)

    
    # Goes to each node and assigns it a random, numerical character label within the bounds of numLabels
    # These labels then get added to the nodeLabels array that is parallel to the nodes array: connecting node to label based on index
    for i in range(len(nodes)):
        nodeLabels.append(random.randint(1, numLabels))


    # Stops iterating through the algorithm when nothing changes or whenever the number of passes equals the number of nodes(stop infinite looping)
    # and numPasses < 5 * (len(nodes) - 1)
    while (stable < len(nodes) and numPasses < (len(nodes) * numLabels)):
        newLabelsArray = nodeLabels.copy()
        stable = 0

        #This is the loop that actually propagates the labels, sorting the graph into communities
        for i in range(len(nodes)):
            print(nodeLabels) #debugging
            nodeLabelOptions = [0] * numLabels
            newLabel = 0
            previousLabel = -1
            
            #Iterates through and retrieves the label of each neighboring node
            for j in range(len(adjacencyLists[str(i)])):
                nodeLabelOptions[nodeLabels[int(adjacencyLists[str(i)][j])] - 1] += 1
            
            print(nodeLabelOptions) #debugging
            #Makes the program not crash from an empty edge list
            if (len(nodeLabelOptions) > 0):
                #Finds the most common connected label
                newLabel = findHighestNum(nodeLabelOptions)
                # Saves previous label to check if anything changed
                previousLabel = nodeLabels[i]
                # Assigns the new label to the newLabelsArray
                newLabelsArray[i] = newLabel
            else:
                #Accounts for entirely isolated nodes
                newLabelsArray[i] = nodeLabels[i]
                stable += 1

            if (previousLabel == newLabel):
                stable = stable + 1
        
        #This format allows the labels to be updated all at once after one pass instead of one at a time. This increases consistency
        nodeLabels = newLabelsArray
        # Increments number of passes to avoid an infinite loop
        numPasses = numPasses + 1
        print("numPasses: " + str(numPasses)) #debugging

    #Prep the output
    for i in range(len(nodes)):
        communitiesArray.append("Node " + str(i) + ": Community " + str(nodeLabels[i]))
    
    print(communitiesArray)
    return communitiesArray

#Simple helper function to find the label with the highest number of counts
def findHighestNum(array):
    tiebreaker = 0
    highestIndex = 0
    for i in range(len(array)):
        if (array[i] > array[highestIndex]):
            highestIndex = i
        #Breaks ties via a coinflip to maintain randomness
        if (array[i] == array[highestIndex]):
            tiebreaker = random.randint(1, 2)
            if (tiebreaker == 2):
                highestIndex = i
    return highestIndex + 1