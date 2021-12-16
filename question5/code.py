# graph
import heapq

test_graph = [[1, 2, 5],
              [2, 3, 6],
              [3, 4, 5],
              [1, 3, 15]]

final_node = 5
    
def shortestReach(graph, final_node):
    # return a list of the starting points
    starting = []
    ending = []
    weights = []
    length = 0
    route = []
    counter = 1
    
    for i in range(0, len(graph)):
        starting.append(graph[i][0])
        ending.append(graph[i][1])
        weights.append(graph[i][2])

    # get the starting point using min
    starting_node = min(min(starting), min(ending))
    ending_node = max(max(starting), max(ending))
    print(starting_node)
    print(ending_node)

    temp_start = starting_node
    temp_end = 0
    temp_weight = 0
    pointer = 0
    while temp_start < ending_node:
        if graph[pointer][0] == temp_start:
            if graph[pointer][2] < temp_weight:
                temp_weight += graph[pointer][2]
                temp_start = graph[pointer][1]
                pointer += 1
                if graph[pointer][1] > temp_end:
                    temp_end = graph[pointer][1]
                if graph[pointer][1] == temp_end:
                    if weigh
        elif graph[pointer][1] == temp_start:
            if graph[pointer][2] < temp_weight:
                temp_weight += graph[pointer][2]
                temp_start = graph[pointer][1]
                pointer += 1
