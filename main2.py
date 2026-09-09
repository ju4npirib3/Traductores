import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import networkx as nx

G = nx.read_weighted_edgelist('toporedes.txt', create_using=nx.Graph())

pos = nx.spring_layout(G, k=0.8, seed=42)
nx.draw(G, with_labels=True, node_size=[G.degree(i) * 100 for i in G.nodes()])

edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, rotate=False)
plt.savefig('grafo.png')