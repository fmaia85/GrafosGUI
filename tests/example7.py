import igraph as ig
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
def plot(graph, visited, current):
    ig.plot(
        graph,
        target=ax,
        vertex_color=["pink" if v == current else "lightblue" if v in visited else "lightgray" for v in g.vs],
        vertex_label=g.vs["name"],
        edge_width=g.es["width"],
        edge_label=g.es["weight"],
        edge_background="white",
    )
    plt.draw()


g = ig.Graph(directed=True)
g.es["color"] = "black"
g.es["width"] = 1.0
g.es["weight"] = 1.0

g.add_vertex(name="Aracajú")
g.add_vertex(name="Fortaleza")
g.add_vertex(name="João Pessoa")
g.add_vertex(name="Maceió")
g.add_vertex(name="Natal")
g.add_vertex(name="Recife")
g.add_vertex(name="Salvador")
g.add_vertex(name="São Luiz")
g.add_vertex(name="Teresina")



g["Aracajú","Maceió"] = 294
g["Aracajú","Salvador"] = 356


g["Fortaleza","João Pessoa"] = 688
g["Fortaleza","Natal"] = 537
g["Fortaleza","Recife"] = 800
g["Fortaleza","Teresina"] = 634

g["João Pessoa","Natal"] = 185
g["João Pessoa","Recife"] = 120
g["João Pessoa","Fortaleza"] = 688

g["Maceió","Aracajú"] = 294
g["Maceió","Recife"] = 285
g["Maceió","Salvador"] = 632


g["Natal","Fortaleza"] = 537
g["Natal","João Pessoa"] = 185


g["Recife","João Pessoa"] = 120
g["Recife","Fortaleza"] = 800
g["Recife","Maceió"] = 285
g["Recife","Salvador"] = 839
g["Recife","Teresina"] = 1137

g["Salvador","Aracajú"] = 356
g["Salvador","Maceió"] = 632
g["Salvador","Recife"] = 839
g["Salvador","Teresina"] = 1163

g["São Luiz","Teresina"] = 446

g["Teresina","São Luiz"] = 446
g["Teresina","Fortaleza"] = 634
g["Teresina","Recife"] = 1137
g["Teresina","Salvador"] = 1163

visited = []
for v in g.vs:
    plot(g, visited, v)
    plt.waitforbuttonpress()
    visited.append(v)


plt.show()