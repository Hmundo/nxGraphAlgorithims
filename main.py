import networkx as nx

def neighbors(G,v):
    N=[]
    for e in E:
        if v==e[0]:
            N.append(e[1])
        elif v==e[1]:
            N.append(e[0])
    return N
    


G = nx.read_edgelist('G.txt')

nx.draw(G)

def V(G):
    return nx.nodes(G)

def E(G):
    return nx.edges(G)
    
def N(G):
    return len(E(G))
    
#def neighbors (G,v):
   # return list (nx.neighbors(G,v))

def degree (G,v):
    return len(nx.neighbors(G,v))
  
def degree_sequence(G):
    D = [degree(G,V) for V in V(G)]    
    D.sort(reverse = True)
    return D
    
def maximum_degree(G):
    return degree_sequence(G)[0]

def minimum_degree(G):
    return degree_sequence(G)[-1]

def avg_degree(G):
    return sum(degree_sequence(G))

print(list(nx.neighbors(G,'5')))
    



    


print(V(G))
print(E(G))
print(N(G))
