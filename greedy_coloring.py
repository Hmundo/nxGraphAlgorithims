import numpy as np
import networkx as nx

def greedy_coloring(G):
    colored_vertices = {v:None for v in V(G)}
    for v in V(G):
        bad_colors = [colored_vertices[w]for w in neigbors(G,v)]
        possible_colors = 1
        while color_vertices as:[v]==None:
def read_graph(name):
    
    E = np.loadtxt(name, dtype = 'int')
    V = []
    for e in E:
        if e[0]:
            V.append(e[0])
        if e[1] not in V:
            V.append(e[0])
    return(V,E)
    G = load_graph('G2.txt')
print(f'VertexList:{[0]}')
print(f'EdgeList:{1}')