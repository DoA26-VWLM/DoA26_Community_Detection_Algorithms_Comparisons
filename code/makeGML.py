#This is just a helper script that can make customizable GML data for use by our main program
#This is not required for our program to run. It is entirely independent, but we thought we'd leave it in


import random
import math
DATAPATH = "../data/"
#Checks to see if a duplicate edge was created. Return true if duplicate. Else, return false
def checkDuplicate(source, target, usedEdges):
    if source == target:
        return True
    if (len(usedEdges[source]) > 0):
        for endNode in usedEdges[source]:
            if target == endNode:
                return True
        return False
    else:
        return False
        


#Takes a number of nodes and a density for edges that is a float between 0 and 1
def makeGML(nodesNum: int, edgesDensity: float, fileName: str):
    currentNodeNumber = 0
    currentEdgesNumber = 0
    edgesNum = math.ceil((edgesDensity * (nodesNum * (nodesNum - 1)) / 2))
    fileObject = open(fileName, "w")
    randomSource = -1
    randomTarget = -1
    usedEdges = {}
    duplicateEdge = False


    #Setup for the start of the file
    fileObject.write("#Nodes: %i, Edges: %i\n" % (nodesNum, edgesNum))
    fileObject.write("graph [\n\tdirected 0\n\n")
    while currentNodeNumber < nodesNum:
        fileObject.write("\tnode [ id %s label \"%s\"] \n" % (str(currentNodeNumber), str(currentNodeNumber)))
        usedEdges[currentNodeNumber] = []
        currentNodeNumber += 1

    #Spaces between nodes and edges
    fileObject.write("\n")
    while currentEdgesNumber < edgesNum:
        #No do-while loop, so do this always once
        randomSource = random.randint(0, nodesNum - 1)
        randomTarget = random.randint(0, nodesNum - 1)
        duplicateEdge = checkDuplicate(randomSource, randomTarget, usedEdges)
        #If the first edge is a duplicate, loop through edge creation until there isn't one
        while duplicateEdge == True:
            randomSource = random.randint(0, nodesNum - 1)
            randomTarget = random.randint(0, nodesNum - 1)
            duplicateEdge = checkDuplicate(randomSource, randomTarget, usedEdges)
        # Because the graph is symmetric, edges need to be tracked symmetrically as well
        usedEdges[randomSource].append(randomTarget)
        usedEdges[randomTarget].append(randomSource)
        fileObject.write("\tedge [ source %i target %i ]\n" % (randomSource, randomTarget))
        currentEdgesNumber += 1

    #Finish the file
    fileObject.write("]")
    fileObject.close()
    return


makeGML(1000, .9, DATAPATH + "graph1000-d90.gml")