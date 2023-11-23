import igraph as ig
import matplotlib.pyplot as plt

# Baseado no exemplo de:
# https://python.igraph.org/en/stable/tutorials/articulation_points.html#sphx-glr-tutorials-articulation-points-py

g = ig.Graph(n=4, edges=[[0, 1], [2, 0]])

fig, ax = plt.subplots()
ig.plot(
    g,
    target=ax,
    vertex_size=30,
    vertex_color="lightblue",
    vertex_label=range(g.vcount()),
    edge_width=0.8,
    edge_color='gray'
)
plt.show()