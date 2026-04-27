# CSC2400: Design of Algorithms Community Detection Algorithms Comparison

## Introduction
This project is over the use and comparison of 4 algorithms to solve the Community Detection problem.

We also included a makeGML.py file that we used to generate our GML data. 

## Running The Program

### Easy Run:

In the ./code folder, there is an executable called "communityDetection.exe". This has everything bundled up into it. Do not move this executable or it will break. 

### Manual Run:

> python ./code/main.py

You may have to use "python3" instead of "python" depending on your interpreter setup. 

Before this is able to be run, you must install the following dependencies(more details below):
- networkx
- chrono
- numpy
- scikit-learn
- easygui

To do this, use the command:

> pip install [package name]

for each package required. 

NOTE: easygui can be slow sometimes. If the program takes a minute to start or GUI windows take longer than expected to open, that is perfectly normal and is outside of our control. The GUI is done by easygui, which although it is very simple, it can be slow and clunky. Furthermore, when you run an algorithm, all program windows will close until the algorithm is done running. This is also normal. The program has not crashed. If you check the console, you will be able to see that the program is still running. This is also due to easygui's implementation. Also, if you run a test on a big dataset, the "continue" button will probably be hidden. You will have to fullscreen the window. Basically, if you see anything weird happening with the GUI, it is likely outside of our control and dependent on the easygui package. We wanted a GUI to make this look nice, but it can be clunky. 

## Problem Description
The Community Detection problem involves taking a graph and identifying groups of nodes called "communities". A community is a collection of nodes that have high interconnectivity within itself with minimal connectivity outside of the community. We will be analyzing, implementing, and comparing the results of 4 algorithms:

- Brute Force
    - Brute Force is used as a baseline function. It has a runtime of Θ(n!), which makes it impractical for any decently sized dataset. Therefore, it is only being used as a baseline for experimental and educational purposes. 
- Label Propagation Algorithm (LPA)
    - This is the first proper algorithm for solving the Community Detection problem.  The Label Propagation Algorithm takes a number of unique tags and applies them randomly to nodes. The algorithm then goes through each node and gives it the tag that the most nodes connected to it have. This causes groups to be formed from nodes that have large amounts of connections, thereby grouping together the unique tags. It has a runtime of Θ(n). LPA sounds like a very good algorithm, however, it has some major issues. It is can be inconsistent with identifying communities due to its randomness, and doesn't always produce great solutions. 
- Spectral Clustering
    - Spectral clustering uses linear algebra to turn a graph into points in lower-dimensional space, then clusters those points. Nodes that are strongly connected end up closer together in this new space. The runtime of Spectral Clusting is Θ(n³). This has a much slower runtime than LPA. However, the solution quality and accuracy is better. 
- Emporeror Penguin Optimizer (EPO)
    - This is our nature-inspired algorithm, inspired by the huddling of Emperor Penguins to preserve heat. This algorithm makes random guesses of communities that continue to improve by copying the best solution. Every iteration, each “penguin” may move a node to a different community, merge, or split groups, with the end goal of moving towards the solution with a bit of randomness to prevent the algorithm from getting stuck. It has a runtime of Θ(I × P × D), where I = Max Iterations, P = Population Size, and D = Number of Dimensions, which is approximately Θ(n) (Two of those values are constants). This algorithm, due to our somewhat messed up implementation of it, does run in linear time, however, the linear time constants that change the emperical runtime end up being huge and dragging out the runtime especially on larger datasets. 

## Team Members
This project was developed collaboratively, with the help of:
- Vincent Pestilli
- Wesley Ni
- Marcus VanWerry

## Dependencies
This project will be using Python and the following libraries:
- networkx
    - Allows for quickly importing and creating graphs from GML without the overhead of hand-jamming graphs and associated methods
- chrono
    - Used for determining runtimes
- numpy
    - Gives advanced mathematical functions, specifically for linear algebra operations in Spectral Clustering
- scikit-learn
    - Gives us access to a K-Means function instead of having to create it from scratch
- easygui
    - Name is self-explanatory. Allows us to create a very simple(albeit slow and clunky) GUI quickly and easily.

## Datasets
Zachary Karate Club GML: "https://gist.github.com/pravj/9168fe52823c1702a07b"
Football Conferences: "https://networkx.org/documentation/stable/auto_examples/graph/plot_football.html"
Flower: https://graphia.app/example-data.html

## Results
Specific results of experimentation can be found in the ./results folder.

The files that are named in the form of "graph[number]-[number]" are randomly generated datasets. The first value is the number of nodes. The second number is the density percentage. For example, "100-50" means 100 nodes with 50% graph density