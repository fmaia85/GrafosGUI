import igraph as ig
import matplotlib.pyplot as plt
import random as rd

fig, ax = plt.subplots()
i = 0
def plot(graph, current, checking, visited, path):
    ax.clear()
    ig.plot(
        graph,
        target=ax,
        vertex_color=["lightgreen" if v == current else "pink" if v in visited else "yellow" if v == checking else "lightgray" for v in graph.vs],
        vertex_label=g.vs["name"],
        edge_width=g.es["width"],
        edge_label=g.es["weight"],
        edge_color=["midnightblue" if e in path else "lightgray" for e in graph.es],
        edge_background="white"
    )
    plt.draw()
    


g = ig.Graph()
g.es["color"] = "black"
g.es["width"] = 1.0
g.es["weight"] = 1.0

g.add_vertex(name="inf")
g.add_vertex(name="inf")
g.add_vertex(name="inf")
g.add_vertex(name="inf")
g.add_vertex(name="inf")
g.add_vertex(name="inf")
g.add_vertex(name="inf")


g[0, 2] = 1
g[2, 1] = 4
g[0, 1] = 2
g[1, 5] = 10
g[1, 4] = 5
g[4, 3] = 2
g[5, 6] = 11
g[3, 5] = 2
g[3, 6] = 1

sourceNode = 0
targetNode = 6
dist = [float('inf') for _ in g.vs]
prev = [None for _ in g.vs]

fila = [i for i in range(7)]
dist[sourceNode] = 0
g.vs[sourceNode]["name"] = "0"
visited = []

while len(fila) > 0:
    curr = -1
    curr_dist = float('inf')
    for i in fila:
        if dist[i] <= curr_dist:
            curr_dist = dist[i]
            curr = i
    fila.remove(curr)
    v = g.vs[curr]

    print(f"Curr:{curr}")

    for e in v.out_edges():
        target = e.target_vertex.index
        if e.target_vertex.index == curr:
            target = e.source_vertex.index

        plot(g, v, g.vs[target], visited, prev)
        plt.waitforbuttonpress()

        if target in fila:
            newDist = dist[curr] + e['weight']
            if(newDist < dist[target]):
                dist[target] = newDist
                prev[target] = e
                g.vs[target]["name"] = f"{newDist}"
                plot(g, v, g.vs[target], visited, prev)
                plt.waitforbuttonpress()
    if curr == targetNode:
        break


    
    
    visited.append(v)


plt.show()