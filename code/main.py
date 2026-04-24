import networkx as nx
import chrono
import BruteForce
import SpectralClustering
import LabelPropagation
import EmperorPenguinOptimizer
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
        print(datasetBoxButton) # debugging
        if datasetBoxButton == None:
            continue
        else:
            #Creates the graph
            graphLink = "../data/" + datasetBoxButton
            graph = nx.read_gml(graphLink)
            
            if algorithmsBoxButton == "Brute Force":
                easygui.msgbox("Your algorithm is about to run. This window will close. Another window will open when your algorithm has been solved", GUITITLE)
                with chrono.Timer() as timed:
                    BruteForce.brute_force_community_detection(graph)
                print(str(round(timed.elapsed, 1)) + " seconds")
            elif algorithmsBoxButton == "Label Propagation":
                easygui.msgbox("Your algorithm is about to run. This window will close. Another window will open when your algorithm has been solved", GUITITLE)
                with chrono.Timer() as timed:
                    LabelPropagation.label_propagation(graph)
                print(str(round(timed.elapsed, 1)) + " seconds")
            elif algorithmsBoxButton == "Spectral Clustering":
                k = easygui.integerbox("Select your k for Spectral Clustering (At least 1)", GUITITLE, lowerbound=1)
                easygui.msgbox("Your algorithm is about to run. This window will close. Another window will open when your algorithm has been solved", GUITITLE)
                with chrono.Timer() as timed:
                    SpectralClustering.spectralClustering(graph, k)
                print(str(round(timed.elapsed, 1)) + " seconds")
            elif algorithmsBoxButton == "Emperor Penguin Optimizer":
                easygui.msgbox("Your algorithm is about to run. This window will close. Another window will open when your algorithm has been solved", GUITITLE)
                with chrono.Timer() as timed:
                    EmperorPenguinOptimizer.emperor_penguin_optimization_community_detection(graph)
                print(str(round(timed.elapsed, 1)) + " seconds")
            else:
                exitProgram = True

easygui.msgbox("Thanks for checking out our algorithms!", GUITITLE)