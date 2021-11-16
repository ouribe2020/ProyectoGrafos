#%%
import networkx as nx  # Importación del paquete NetworkX
import matplotlib.pyplot as plt  # Importación paquete Matplotlib con el módulo pyplot


G = nx.random_regular_graph(5, 10)  # Función generadora de un grafo d-regular random de n vértices
nx.draw_kamada_kawai(G, node_size=50, width=0.5, with_labels=False)  # Dibujar el grafo G con una interfaz particular
plt.axis("equal")  # Redimensionar los ejes a longitudes iguales
plt.show()  # Mostrar el grado d-regular por pantalla
