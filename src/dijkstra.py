from igraph import Graph
from customPlot import CustomPlot

def initPathArray(n:int):
    return [None for _ in range(n)]
#}initPathArray

def findClosestOnFila(fila):
    currV = None
    curr_dist = float('inf')
    for v in fila:
        if float(v["name"]) <= curr_dist:
            curr_dist = float(v["name"])
            currV = v
        #}if
    #}for
    fila.remove(currV)
    return currV
#}findClosestOnFila

def run(graph:Graph, sourceId, targetId):
    cp = CustomPlot()

    path = initPathArray(len(graph.vs))
    fila = list(graph.vs)
    visited = []
    graph.vs[sourceId]["name"] = "0"

    while len(fila) > 0:
        currV = findClosestOnFila(fila)
        for n in currV.neighbors():
            cp.plotDijkstra(graph, currV, n, visited, path)
            if n in fila:
                e = graph.es[graph.get_eid(currV, n)]
                newDist = float(currV["name"]) + e['weight']
                if(newDist < float(n["name"])):
                    n["name"] = f"{newDist:.0f}"
                    path[n.index] = e
                    cp.plotDijkstra(graph, currV, n, visited, path)
                #}if
            #}if
        #}for
        visited.append(currV)
        if currV.index == targetId:
            break
        #}if
    #}while
    cp.keepShowing()
#}run
