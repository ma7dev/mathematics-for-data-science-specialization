# Instructions

The program you write should do the following.

1. Read the example of the social network graph from the SNAP dataset (facebook_combined.txt)
2. Compute the ACC for this graph.
3. Compute the probability of an edge between two random vertices in the graph, by dividing the number of edges by the maximal possible number of edges. Denote this probability by P.
4. Generate an Erdős–Rényi random graph with the same number of vertices as the original graph. An edge between two vertices is drawn with probability P (and not drawn with probability (1-P)), independently for each pair of vertices.
5. Compute the ACC for the random graph.
6. Compare the results.

The resulting output should consist of two numbers, the ACC of the original graph and the ACC of the random graph. For debugging purposes, it is useful to see other parameters, such as the number of edges in the random graph (it should be close to the number of edges in the original graph).