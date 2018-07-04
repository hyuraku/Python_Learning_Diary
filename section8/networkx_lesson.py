import matplotlib.pyplot as plt
import networkx as nx

G = nx.Graph()
G.add_node(1)

G.add_nodes_from([2,3,4,5])

G.add_edge(1,3)
G.add_edge(3,5)
G.add_edge(5,2)
G.add_edge(2,4)
G.add_edge(4,1)

nx.draw(G)
plt.show()
