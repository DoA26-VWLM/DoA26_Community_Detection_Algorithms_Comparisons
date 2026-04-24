import networkx as nx
import chrono
import BruteForce
import SpectralClustering
import helperFunctions
import easygui
import LabelPropagation

#GRAPHLINK = "../data/karateGraphGithub.gml"
GRAPHLINK = "../data/test.gml"

newGraph: nx.Graph = nx.read_gml(GRAPHLINK)

#LabelPropagation.labelPropagation(newGraph, 4)
#SpectralClustering.spectralClustering(newGraph, 4)
#BruteForce.brute_force_community_detection(newGraph)

print(LabelPropagation.label_propagation(newGraph))