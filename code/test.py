from node import *
import networkx as nx
import chrono

GRAPHLINK = "../data/karateGraphGithub.txt"

newGraph = nx.read_gml(GRAPHLINK)

print(newGraph)
#newGraph.nodes[1]

