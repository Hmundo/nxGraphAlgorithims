import networkx as nx
from local_properties import degree
def V(G):
    return nx.nodes(G)

def E(G):
    return nx.edges(G)

def radius(G):
    return nx.radius(G)

def diameter(G):
    return nx.diameter(G)   

def n(G):
    return len(E(G))
    
def degree_sequence(G):
    D = [degree(G,v) for v in V(G)]    
    D.sort(reverse = True)
    return D
    
def maximum_degree(G):
    return degree_sequence(G)[0]

def minimum_degree(G):
    return degree_sequence(G)[-1]

def avg_degree(G):
    return sum(degree_sequence(G))