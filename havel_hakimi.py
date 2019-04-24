import networkx as nx 

def havel_hakimi_graph(deg_sequence):
    
    N = len(deg_sequence)
    G = networkx.empty_graph(N) 

    if N==0 or max(deg_sequence)==0: 
        return G 