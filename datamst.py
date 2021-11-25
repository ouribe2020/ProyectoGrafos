import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms import tree
from covid19dh import covid19
from datetime import date
import math
import mpu

def mst(nomb, paises):
    #G = nx.complete_graph(nomb)
    G = nx.Graph()

    for x in range(len(nomb)):
        for y in range(len(nomb)-1):
            if(nomb[x] != nomb[y]):
                G.add_edge(nomb[x], nomb[y], weight=mpu.haversine_distance(paises[x], paises[y]))
    # G.add_edge('A', 'B', weight=4)


    #pos = nx.spring_layout(G)
    pos = nx.circular_layout(G)
    # #camino mas corto entre nodos
    # dj = nx.dijkstra_path(G, source = 'D', target = 'A')
    # print(list(dj))

    # Camino minimo
    mst = tree.minimum_spanning_edges(G, algorithm="kruskal", data=False)
    return(list(mst))

    # nx.draw(G, pos, with_labels = True)
    # nx.draw_networkx_edge_labels(G, pos)

    # plt.draw()
    # plt.show()