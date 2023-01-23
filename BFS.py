# Implementation of Breadth First Search

graph = {
        "5" : ['3','7'],
        "4" : ['5','6'],
        "3" : ['7','8'],
        "7": ['8'],
        "8" : []
        }

visited = []
unvisited = []

def bfs(visited, graph, node):
    visited.append(node)
    unvisited.append(node)

    while unvisited:
        m = unvisited.pop(0)
        print(m)

        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                unvisited.append(neighbour)


bfs(visited, graph, "5")

