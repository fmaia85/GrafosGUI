import igraph as ig
import matplotlib.pyplot as plt

# Baseado no exemplo de:
# https://python.igraph.org/en/stable/tutorials/articulation_points.html#sphx-glr-tutorials-articulation-points-py

g = ig.Graph.Formula(
    "Br:Pa:Bo:Ar-Br:Pa:Bo:Ar, Br:Ar:Ur-Br:Ar:Ur",
)

articulation_points = g.vs[g.articulation_points()]

fig, ax = plt.subplots()
ig.plot(
    g,
    target=ax,
    vertex_size=30,
    vertex_color="lightblue",
    vertex_label=g.vs["name"],
    vertex_frame_color = ["red" if v in articulation_points else "black" for v in g.vs],
    vertex_frame_width = [3 if v in articulation_points else 1 for v in g.vs],
    edge_width=0.8,
    edge_color='gray'
)
plt.show()