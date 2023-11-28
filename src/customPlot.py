import igraph as ig
import matplotlib.pyplot as plt

class CustomPlot:

    def __init__(self) -> None:
        self.fig, self.ax = plt.subplots()

    def plotDijkstra(self, graph, current, checking, visited, path):
        self.ax.clear()
        ig.plot(
            graph,
            target=self.ax,
            vertex_color=["lightgreen" if v == current else "pink" if v in visited else "yellow" if v == checking else "lightgray" for v in graph.vs],
            vertex_label=graph.vs["name"],
            edge_width=graph.es["width"],
            edge_label=graph.es["weight"],
            edge_color=["midnightblue" if e in path else "lightgray" for e in graph.es],
            edge_background="white"
        )
        plt.draw()
        plt.waitforbuttonpress()
    
    def keepShowing(self):
        plt.show()