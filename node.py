"""
This file will define the custom node class for use throughout this project
"""

class Node:
    def __init__(self, identifier: str, label: str = "", connections: list[str] = []):
        self.__identifier = identifier
        self.__label = label
        self.__connections = connections

    # Getters
    def getIdentifier(self):
        return self.__identifier
    
    def getLabel(self):
        return self.__label
    
    def getConnections(self):
        return self.__connections
    
    # Setters
    def setIdentifier(self, value):
        self.__identifier = value

    def setLabel(self, value):
        self.__label = value

    # Methods
    def addConnection(self, newConnectionName):
        self.__connections.append(newConnectionName)

    def printInformation(self):
        print("Information on Node %s" % self.__identifier)
        if self.__label != "":
            print("Node label is %s" % self.__label)
        if len(self.__connections) == 0:
            print("This Node has no connections")
        else:
            for connection in self.__connections:
                print("Node %s is connected to Node %s" % (self.__identifier, connection))
    
 
