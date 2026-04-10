import networkx as nx
import chrono
import BruteForce

edgeArray = []

#GRAPHLINK = "../data/karateGraphGithub.txt"
GRAPHLINK = "../data/test.gml"

newGraph: nx.Graph = nx.read_gml(GRAPHLINK) 

#print(newGraph.nodes(data=True))
print("\n")
print(newGraph.edges)

for edge in newGraph.edges:
    edgeArray.append(edge)


print("\n\n")
BruteForce.brute_force_community_detection(edgeArray)