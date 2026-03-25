from node import *
import networkx as nx
import chrono

GRAPHLINK = "karateGraphGithub.txt"

newGraph = nx.read_gml(GRAPHLINK)

print(newGraph)
#newGraph.nodes[1]

