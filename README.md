# DoA26_Community_Detection

## Introduction
This project is over the use and comparison of runtimes of 4 algorithms attempting to solve the Community Detection problem.

The Community Detection problem involves taking a graph and identifying groups of nodes called "communities". A community is a collection of nodes that have high interconnectivity within itself with minimal connectivity outside of the community. We will be analyzing, implementing, and comparing 4 algorithms:

- Brute Force
    - Brute Force is used as a baseline function. It has a runtime of Θ(2n), which makes it impractical for any decently sized dataset. Therefore, it is only being used as a baseline for experimental and educational purposes. 
- Label Propagation Algorithm (LPA)
    - This is the first proper algorithm for solving the Community Detection problem.  The Label Propagation Algorithm takes a number of unique tags and applies them randomly to nodes. The algorithm then goes through each node and gives it the tag that the most nodes connected to it have. This causes groups to be formed from nodes that have large amounts of connections, thereby grouping together the unique tags. It has a runtime of Θ(n). LPA sounds like a very good algorithm, however, it has some major issues. It is can be inconsistent with identifying communities due to its randomness, and doesn't always produce great solutions. 
- Spectral Clustering
    - Spectral clustering uses linear algebra to turn a graph into points in lower-dimensional space, then clusters those points. Nodes that are strongly connected end up closer together in this new space. The runtime of Spectral Clusting is Θ(n³). This has a much slower runtime than LPA. However, the solution quality and accuracy is better. 
- Emporeror Penguin Optimizer (EPO)
    - This is our nature-inspired algorithm, inspired by the huddling of Emperor Penguins to preserve heat. This algorithm makes random guesses of communities that continue to improve by copying the best solution. Every iteration, each “penguin” may move a node to a different community, merge, or split groups, with the end goal of moving towards the solution with a bit of randomness to prevent the algorithm from getting stuck. It has a runtime of Θ(I × P × D), where I = Max Iterations, P = Population Size, and D = Number of Dimensions, which is approximately Θ(n³).0

## Dependencies
This project will be using Python and the following libraries:
- NetworkX
- Chrono

## Datasets
Zachary Karate Club GML: "https://gist.github.com/pravj/9168fe52823c1702a07b"
