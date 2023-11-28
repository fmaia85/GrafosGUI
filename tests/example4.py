import random
import igraph as ig
import matplotlib.pyplot as plt

# Baseado no exemplo de:
# https://python.igraph.org/en/stable/tutorials/articulation_points.html#sphx-glr-tutorials-articulation-points-py

random.seed(0)
g = ig.Graph.Lattice([4, 4], circular=False)
g.es["weight"] = [random.randint(1, 20) for edge in g.es]

mst_edges = g.spanning_tree(weights=g.es["weight"], return_tree=False)

print("Minimum edge weight sum:", sum(g.es[mst_edges]["weight"]))

g.es["color"] = "lightgray"
g.es[mst_edges]["color"] = "midnightblue"
g.es["width"] = 1.0
g.es[mst_edges]["width"] = 3.0

fig, ax = plt.subplots()
ig.plot(
    g,
    target=ax,
    layout="grid",
    vertex_color="lightblue",
    edge_width=g.es["width"],
    edge_label=g.es["weight"],
    edge_background="white",
)
plt.show()