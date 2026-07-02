import numpy as np

# Define the graph edges (from → to)
edges = {
    'a': ['b', 'c'],
    'b': ['d'],
    'c': ['a', 'b', 'd'],
    'd': ['c']
}

nodes = list(edges.keys())
N = len(nodes)

# Map nodes to indices
node_index = {node: i for i, node in enumerate(nodes)}

# Create adjacency matrix M: M[j][i] = 1 if node i points to node j
M = np.zeros((N, N))

for i, node in enumerate(nodes):
    outlinks = edges[node]
    for dest in outlinks:
        j = node_index[dest]
        M[j][i] = 1

# Normalize columns (handle dangling nodes)
for i in range(N):
    col_sum = np.sum(M[:, i])
    if col_sum != 0:
        M[:, i] /= col_sum
    else:
        # Dangling node: distribute evenly
        M[:, i] = 1.0 / N

# PageRank parameters
damping_factor = 0.85
epsilon = 1e-6

# Initialize rank vector
r = np.ones(N) / N

# Iterate until convergence
delta = 1
while delta > epsilon:
    r_new = (1 - damping_factor) / N + damping_factor * M @ r
    delta = np.linalg.norm(r_new - r, 1)
    r = r_new

# Print PageRank scores
for node, rank in zip(nodes, r):
    print(f"PageRank of {node}: {rank:.4f}")
