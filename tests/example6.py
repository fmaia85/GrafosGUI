import igraph as ig
import matplotlib.pyplot as plt


g = ig.Graph(directed=True)
g.add_vertex(name="a")
g.add_vertex(name="b")
g.add_vertex(name="c")
g.add_vertex(name="d")
g.es["weight"] = 1.0


g["a","b"] = 15
g["a","c"] = 34
g["a","d"] = 10
g["d","c"] = 6
g["c","b"] = 7

for v in g.vs:
    print(f"{v['name']}")

    print(f"Lista de vizinhos: {v.out_edges()}")
    for e in v.out_edges():
        print(f"{e.target_vertex.index}", end=" ")
    print("\n")

for e in g.es:
    print(f"{e.source_vertex['name']}", end="-")
    print(f"{e.target_vertex['name']}", end=":")
    print(f"{e['weight']}")

vertex_a = g.vs.find(name='a')
print(f"Achando a: {vertex_a}")
for e in vertex_a.all_edges():
    print(f"{e.source_vertex['name']}", end="-")
    print(f"{e.target_vertex['name']}", end=":")
    print(f"{e['weight']}")
    

g.es["color"] = "black"
g.es["width"] = 1.0

fig, ax = plt.subplots()
ig.plot(
    g,
    target=ax,
    vertex_color=["lightblue" if v["name"] == "a" else "lightgray" for v in g.vs],
    vertex_label=g.vs["name"],
    edge_width=g.es["width"],
    edge_label=g.es["weight"],
    edge_background="white",
)
plt.show()