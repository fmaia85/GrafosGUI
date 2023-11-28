import dijkstra
import igraph as ig

g = ig.Graph(n=7)
g.es["color"] = "black"
g.es["width"] = 1.0
g.es["weight"] = 1.0

for v in g.vs:
    v["name"] = "inf"

g[0, 2] = 1
g[2, 1] = 4
g[0, 1] = 2
g[1, 5] = 10
g[1, 4] = 5
g[4, 3] = 2
g[5, 6] = 11
g[3, 5] = 2
g[3, 6] = 1


dijkstra.run(g, 0, 6)

