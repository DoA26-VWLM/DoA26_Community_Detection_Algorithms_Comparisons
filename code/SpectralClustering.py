"""
    This section of code defines logic for finding communities via spectral clustering, 
    which uses k-Means clustering on a Laplacian Matrix to find communities
"""
import numpy.linalg as np
from sklearn.cluster import KMeans
import networkx as nx

def spectralClustering(graph: nx.Graph, k: int):
    #Array for clean outputs
    nodesOutputArray = []
    strangeArray = []
    labelNum = 0
    #Gets the normalized Laplacian matrix to identify connectivity of nodes
    #The toarray() method changes the matrix from a SciPy sparse array (which is space efficient but not used for calculations)
    #Into a traditional, 2d array for calculations
    laplacianMatrix = nx.normalized_laplacian_matrix(graph).toarray()
    print(laplacianMatrix)
    
    eigVal, eigVec = np.eigh(laplacianMatrix)
    eigVec = eigVec[:, 0:k]

    print("\n\n\n")
    print("New Eigens")
    print(eigVec)


    row_norms = np.norm(eigVec, axis=1, keepdims=True)
    
    # Avoid division by zero
    row_norms[row_norms == 0] = 1
    
    eigVec_normalized = eigVec / row_norms

    #Construct an object k means with 
    kmeans = KMeans(n_clusters=k)
    labelsNorm = kmeans.fit_predict(eigVec_normalized)
    print("\n\nLabels\n")
    print(labelsNorm)

    labelsStrange = kmeans.fit_predict(eigVec)
    print("\n\nLabels Strange\n")
    print(labelsStrange)


    for label in labelsNorm:
        nodeLabel = "Node " + str(labelNum) + " : Group " + str(labelsNorm[labelNum])
        nodesOutputArray.append(nodeLabel)
        labelNum += 1

    #Below is for testing
    labelNum = 0
    for label in labelsStrange:
        nodeLabel = "Node " + str(labelNum) + " : Group " + str(labelsStrange[labelNum])
        strangeArray.append(nodeLabel)
        labelNum += 1
    

    print(nodesOutputArray)
    return nodesOutputArray
