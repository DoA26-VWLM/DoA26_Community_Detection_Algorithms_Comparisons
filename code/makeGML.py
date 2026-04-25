#Makes a GML file
import random
import math
DATAPATH = "../data/"

#Takes a number of nodes and a density for edges that is a float between 0 and 1
def makeGML(nodesNum: int, edgesDensity: float, fileName: str):
    currentNodeNumber = 0
    currentEdgesNumber = 0
    edgesNum = math.ceil((nodesNum * (nodesNum - 1)) / 2)
    fileObject = open(fileName, "w")
    randomSource = -1
    randomTarget = -1
    usedEdges = {}
    
    #Setup for the start of the file
    fileObject.write("#Nodes: %i, Edges: %i\n" % (nodesNum, edgesNum))
    fileObject.write("graph [\n\tdirected 0\n\n")
    while currentNodeNumber < nodesNum:
        fileObject.write("\tnode [ id %s label \"%s\"] \n" % (str(currentNodeNumber), str(currentNodeNumber)))
        currentNodeNumber += 1

    #Spaces between nodes and edges
    fileObject.write("\n")
    while currentEdgesNumber < edgesNum:
        randomSource = random.randint(0, nodesNum - 1)
        randomTarget = random.randint(0, nodesNum - 1)
        fileObject.write("\tedge [ source %i target %i ]\n" % (randomSource, randomTarget))
        currentEdgesNumber += 1

    #Finish the file
    fileObject.write("]")
    fileObject.close()
    return


makeGML(100, .1, DATAPATH + "test100")