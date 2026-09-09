#!/usr/bin/python
# -*- coding: utf-8 -*-
#from pylab import figure
import pylab #matplotlib descargar
import networkx as nx
G=nx.read_weighted_edgelist('toporedes.txt', create_using=nx.Graph())
nx.draw(G, with_labels=True, node_size = [G.degree(i) * 100 for i in G.nodes()])
diam= nx.diameter(G)
node_degree = nx.degree(G)
pylab.show()
