import networkx as nx
import chrono
import BruteForce
import SpectralClustering
import LabelPropagation
import helperFunctions
import easygui
import os

# Constants and Variables
GUITITLE = "Community Detection Algorithm Comparisons"
OKBUTTON = "Continue"
exitProgram = False
algorithmsBoxButton = ""
datasetBoxButton = ""
graphLink = ""
graph: nx.Graph
labels = 0
k = 0
datasets = None

# Intro window
easygui.msgbox("Welcome to our Community Detection Algorithms comparison!\nThis was made for our CSC2400 Design of Algorithms class by Vincent Pestilli, Wesley Ni, and Marcus VanWerry", GUITITLE, ok_button=OKBUTTON)

# Main program loop
while (exitProgram == False):
    algorithmsBoxButton = easygui.buttonbox("Which algorithm would you like to run?", GUITITLE, ["Brute Force", "Label Propagation", "Spectral Clustering", "Emperor Penguin Optimizer", "Exit Program"])
    if algorithmsBoxButton == "Exit Program" or algorithmsBoxButton == None:
        exitProgram = True
    else:
        # Updates the list of datasets from data directory every time this is called
        datasets = os.listdir("../data")
        datasetBoxButton = easygui.choicebox("Which datset would you like to use? (Pulled from ../data/*)", GUITITLE, datasets)
        if datasetBoxButton == None or datasetBoxButton == "Exit Program":
            exitProgram = True
        else:
            #Creates the graph
            graphLink = "../data/" + datasetBoxButton
            graph = nx.read_gml(graphLink)
            easygui.msgbox("Your algorithm is about to run. This window will close. Another window will open when your algorithm has been solved", GUITITLE)
            if algorithmsBoxButton == "Brute Force":
                BruteForce.brute_force_community_detection(graph)
            elif algorithmsBoxButton == "Label Propagation":
                LabelPropagation.label_propagation(graph)
            elif algorithmsBoxButton == "Spectral Clustering":
                k = easygui.integerbox("Select your k for Spectral Clustering (At least 1)", GUITITLE, lowerbound=1)
                SpectralClustering.spectralClustering(graph, k)
            elif algorithmsBoxButton == "Emperor Penguin Optimizer":
                pass
            else:
                exitProgram = True

easygui.msgbox("Thanks for checking out our algorithms!", GUITITLE)