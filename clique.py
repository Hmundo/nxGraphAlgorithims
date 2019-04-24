import networkx as nx

from itertools import combinations
from functions.global_properties import V
from functions.local_properties import neighbors

G = nx.read_edgelist('graph_library/pan.txt')
nx.draw(G)


def is_clique(G,S):
    for v in S:
        if list(set(S) & set(neighbors(G,v))) != []:
            return True
    return False
    
def maximum_clique_set(G):
        n = len(V(G))
        for k in range(n,1,-1):
            for S in combinations(V(G),k):
                if is_clique(G,list(S))== True:
                    return list(S)
                
def clique_numbers(G):
    return len(maximum_clique_set(G))

print(maximum_clique_set(G))