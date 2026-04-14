import networkx as nx
import chrono
import BruteForce
import SpectralClustering

edgeArray = []

GRAPHLINK = "../data/karateGraphGithub.gml"
#GRAPHLINK = "../data/test.gml"

newGraph: nx.Graph = nx.read_gml(GRAPHLINK)

#print(newGraph.nodes(data=True))
print("\n")
print(newGraph.edges)

for edge in newGraph.edges:
    edgeArray.append(edge)


#print(nx.laplacian_matrix(newGraph))
print("\n\n")
SpectralClustering.spectralClustering(newGraph, 4)
#BruteForce.brute_force_community_detection(edgeArray)