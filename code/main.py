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
detectedCommunities = None
outputFileName = ""
saveFile = None
fileObject = None
chosenAlgorithm = ""
prettyCommunities = ""
modPrepArray = []
modScore = None


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
        if datasetBoxButton == None:
            continue
        else:

            #Creates the graph
            graphLink = "../data/" + datasetBoxButton
            graph = nx.read_gml(graphLink)

            if algorithmsBoxButton == "Brute Force":
                chosenAlgorithm = "Brute Force"
                easygui.msgbox("Your algorithm is about to run. This window will close. Another window will open when your algorithm has been solved", GUITITLE)
                with chrono.Timer() as timed:
                    detectedCommunities = BruteForce.brute_force_community_detection(graph)
            elif algorithmsBoxButton == "Label Propagation":
                chosenAlgorithm = "Label Propagation"
                easygui.msgbox("Your algorithm is about to run. This window will close. Another window will open when your algorithm has been solved", GUITITLE)
                with chrono.Timer() as timed:
                    detectedCommunities = LabelPropagation.label_propagation(graph)
            elif algorithmsBoxButton == "Spectral Clustering":
                chosenAlgorithm = "Spectral CLustering"
                k = easygui.integerbox("Select your k for Spectral Clustering (At least 1)", GUITITLE, lowerbound=1)
                easygui.msgbox("Your algorithm is about to run. This window will close. Another window will open when your algorithm has been solved", GUITITLE)
                with chrono.Timer() as timed:
                    detectedCommunities = SpectralClustering.spectralClustering(graph, k)
            elif algorithmsBoxButton == "Emperor Penguin Optimizer":
                chosenAlgorithm = "Emperor Penguin Optimization"
                easygui.msgbox("Your algorithm is about to run. This window will close. Another window will open when your algorithm has been solved", GUITITLE)
                with chrono.Timer() as timed:
                    detectedCommunities = EmperorPenguinOptimizer.emperor_penguin_optimization_community_detection(graph)
            else:
                exitProgram = True

        #Calculate modularity
        modPrepArray = helperFunctions.prepForMod(detectedCommunities)
        modScore = helperFunctions.modularity(nx.adjacency_matrix(graph).toarray(), modPrepArray)
        # Results of algorithm
        easygui.msgbox("Your algorithm of choice took " + f"{timed.elapsed:.6f}" + " seconds to execute for the chosen dataset. The results will be shown on the next window", GUITITLE)
        prettyCommunities = helperFunctions.prettifyCommunities(detectedCommunities)
        easygui.msgbox("The communities your algorithm detected are:\n" + prettyCommunities + "\nYour algorithm had a modularity score of: " + f"{modScore:.6f}", GUITITLE)
        #Saving to an output file
        saveFile = easygui.ynbox("Would you like to save your results to a file?", GUITITLE)
        if saveFile == True:
            outputFileName = easygui.textbox("What would you like to name your output file?", GUITITLE)
            if outputFileName != None:
                file = open("../results/" + outputFileName + ".txt", "w")
                file.write("Community Detection Report:\nAlgorithm: " + chosenAlgorithm + "\nDataset: " + datasetBoxButton + "\nTime: " + f"{timed.elapsed:.6f}" + " seconds\n" + "Modularity: " + f"{modScore:.6f}" + "\n")
                file.write(prettyCommunities)
                file.close()
                easygui.msgbox("Your results have been saved in the results folder!", GUITITLE)

easygui.msgbox("Thanks for checking out our algorithms!", GUITITLE)