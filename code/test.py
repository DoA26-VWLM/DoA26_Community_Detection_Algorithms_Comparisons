import networkx as nx
import chrono
import BruteForce
import SpectralClustering
import LabelPropagation
import helperFunctions

edgeArray = []

GRAPHLINK = "../data/karateGraphGithub.gml"
#GRAPHLINK = "../data/test.gml"

newGraph: nx.Graph = nx.read_gml(GRAPHLINK)

print("\n")

edgeArray = helperFunctions.getEdges(newGraph)

print("\n\n")

LabelPropagation.labelPropagation(newGraph, 5)