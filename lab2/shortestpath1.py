# lab 2.1
#https://liu.kattis.com/courses/AAPS/AAPS23/assignments/iny8rp/problems/shortestpath1

import sys
import heapq
from pprint import pprint

def dijkstra(edge_list, start_node):
    # Initialize distances to all nodes as infinite except for the start node, which is 0
    distances = {node: float('inf') for node in set(sum(([edge[0], edge[1]] for edge in edge_list), []))}
    distances[start_node] = 0

    # Use a min heap to keep track of the next node to visit
    heap = [(0, start_node)]

    # Use a dictionary to keep track of the shortest path to each node
    shortest_paths = {start_node: [start_node]}

    while heap:
        # Get the node with the smallest distance from the heap
        current_distance, current_node = heapq.heappop(heap)

        # Skip nodes that have already been visited
        if current_distance > distances[current_node]:
            continue

        # Update the distances to all neighboring nodes
        for edge in edge_list:
            if edge[0] == current_node:
                neighbor = edge[1]
                distance = current_distance + edge_list[edge]
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    shortest_paths[neighbor] = shortest_paths[current_node] + [neighbor]
                    heapq.heappush(heap, (distance, neighbor))

    # Return both the shortest distances and shortest paths
    return distances, shortest_paths

start = True
n = 0
m = 0
q = 0
s = 0
m_left = 0
q_left = 0
edges = {}

shortest_path = {}
total_weight = {}
for line in sys.stdin:
    line = line.split()
    # Read first line of test-case
    if len(line) > 3:
        n, m, q, s = int(line[0]), int(line[1]), int(line[2]), int(line[3])
        if n == m == q == s == 0:
            break
        # Empty print after to separate test-cases
        elif not start:
            print()
        start = False
        m_left = m
        q_left = q
    # Read edges and put them in edges dict
    elif m_left:
        edges[(int(line[0]), int(line[1]))] = int(line[2])
        m_left -= 1
        # Contruct shortest paths to every node and save
        if not m_left:
            total_weight, shortest_path = dijkstra(edges, s)
    # Read shortest paths and distances for every query
    elif q_left:
        query = int(line[0])
        q_left -= 1
        if query not in shortest_path:
            print("Impossible")
        else:
            print(total_weight[query])
        if not q_left:
            edges = {}