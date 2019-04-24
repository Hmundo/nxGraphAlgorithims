import networkx as nx

def matching(G2):
    
    E = np.loadtxt(G2, dtype = 'int')
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