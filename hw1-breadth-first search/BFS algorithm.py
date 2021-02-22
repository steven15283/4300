
graph = {}
graph['Sibiu'] = ['Fagaras', 'Rimnicu Vilcea']
graph['Fagaras'] = ['Sibiu', 'Bucharest']
graph['Rimnicu Vilcea'] = ['Sibiu', 'Pitesti', 'Craiova']
graph['Pitesti'] = ['Rimnicu Vilcea', 'Craiova', 'Bucharest']
graph['Craiova'] = ['Rimnicu Vilcea', 'Pitesti']
graph['Bucharest'] = ['Fagaras', 'Pitesti', 'Giurgiu']
graph['Giurgiu'] = ['Bucharest']


def shortest_path_BFS(graph, start, goal):
    visited = []#this is the list of all visited cities

    queue = [[start]]#this is the initialized list of the FIFO queue and it keeps track of the path

    while queue:
        path = queue.pop(0)#get node in queue for path
        node = path[-1]#get node before path

        if node not in visited:#when the node is not in visited
            neighbours = graph[node]#get next layer from graph

            for neighbour in neighbours:
                new_path = list(path)#create new path
                new_path.append(neighbour)#add neighbour to path(traverse)
                queue.append(new_path)#add new path to the queue

            if neighbour == goal:
                print(new_path)#print path(solution)
                return

            visited.append(node)

# Call shortest_path_BFS
shortest_path_BFS(graph, 'Sibiu', 'Bucharest')