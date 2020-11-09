import networkx as nx
from random import random

# Read data from the dataset, and create graph G_fb
G_fb = nx.read_edgelist("facebook_combined.txt", create_using = nx.Graph(), nodetype=int)

# Show the number of edges in G_fb
print("edges = " + str(G_fb.number_of_edges()))

# Show number of nodes in G_fb
print("nodes = " + str(G_fb.number_of_nodes()))

# TASK1. Now your task is to compute the probability whether there is an edge between two vertices.
# e/(n * (n-1) /2)
edge_probab = G_fb.number_of_edges()/(G_fb.number_of_nodes()*(G_fb.number_of_nodes()-1)/2)

# TASK2. Compute the ACC (average clustering coefficient) of G_fb
# (consult the NetworkX manual or the video lecture for the correct function which does it)
av_clust_coeff =  nx.average_clustering(G_fb)
print("fbgraph_acc = " + str(av_clust_coeff))

# Now we have to generate a random graph. First we initialize it
G_rand = nx.Graph()

# TASK3. generate edges in G_rand at random:
for i in range(0,G_fb.number_of_nodes()) :
    for j in range(0,i) :
        # Add an edge between vertices i and j, with probability edge_probab (as in G_fb)
        r = random()
        if(r <= edge_probab):
            G_rand.add_edge(i,j)

# Now we print out the number of edges and the ACC of the new graph
print("rgraph_edges = " + str(G_rand.number_of_edges()))

av_clust_coeff = nx.average_clustering(G_rand)

print("rgraph_acc = " + str(av_clust_coeff))

# The results which should be submitted to the grader include the ACC of G_fb and of G_rand. Good luck!
