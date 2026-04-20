import networkx as nx
import chrono
import BruteForce
import SpectralClustering
import LabelPropagation
import helperFunctions

edgeArray = []

#GRAPHLINK = "../data/karateGraphGithub.gml"
GRAPHLINK = "../data/test.gml"

newGraph: nx.Graph = nx.read_gml(GRAPHLINK)

edgeArray = helperFunctions.getEdges(newGraph)

LabelPropagation.labelPropagation(newGraph, 4)
#SpectralClustering.spectralClustering(newGraph, 4)
#BruteForce.brute_force_community_detection(edgeArray)