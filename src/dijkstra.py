from igraph import Graph
from customPlot import CustomPlot

def initDistArray(n:int):
    return [float('inf') for _ in range(n)]

def initPathArray(n:int):
    return [None for _ in range(n)]

def initFilaArray(n:int):
    return [i for i in range(n)]

def run(graph:Graph, sourceId, targetId):
    dist = initDistArray(len(graph.vs))
    path = initPathArray(len(graph.vs))
    fila = initFilaArray(len(graph.vs))

    cp = CustomPlot()

    dist[sourceId] = 0
    graph.vs[sourceId]["name"] = "0"
    visited = []

    while len(fila) > 0:
        currVid = -1
        curr_dist = float('inf')
        for i in fila:
            if dist[i] <= curr_dist:
                curr_dist = dist[i]
                currVid = i
        fila.remove(currVid)
        v = graph.vs[currVid]

        for e in v.out_edges():
            target = e.target_vertex.index
            if e.target_vertex.index == currVid:
                target = e.source_vertex.index

            cp.plotDijkstra(graph, v, graph.vs[target], visited, path)

            if target in fila:
                newDist = dist[currVid] + e['weight']
                if(newDist < dist[target]):
                    dist[target] = newDist
                    path[target] = e
                    graph.vs[target]["name"] = f"{newDist}"
                    cp.plotDijkstra(graph, v, graph.vs[target], visited, path)
        visited.append(v)
        if currVid == targetId:
            break


    cp.keepShowing()
