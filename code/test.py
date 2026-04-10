import networkx as nx
import chrono

GRAPHLINK = "../data/karateGraphGithub.txt"

newGraph: nx.Graph = nx.read_gml(GRAPHLINK) 

print(newGraph.nodes(data=True))