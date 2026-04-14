"""
    This section of code defines logic for finding communities via spectral clustering, 
    which uses k-Means clustering on a Laplacian Matrix to find communities
"""
import numpy.linalg

def spectralClustering():
    