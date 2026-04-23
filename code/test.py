import networkx as nx
import chrono
import BruteForce
import SpectralClustering
import LabelPropagation
import helperFunctions
import easygui

#GRAPHLINK = "../data/karateGraphGithub.gml"
GRAPHLINK = "../data/test.gml"

newGraph: nx.Graph = nx.read_gml(GRAPHLINK)

#LabelPropagation.labelPropagation(newGraph, 4)
#SpectralClustering.spectralClustering(newGraph, 4)
BruteForce.brute_force_community_detection(newGraph)