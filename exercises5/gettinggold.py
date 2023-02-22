# getting gold 
# https://liu.kattis.com/courses/AAPS/AAPS23/assignments/vz3dkh/problems/gold

from pprint import pprint

def bfs(visited, graph, node):
    visited.append(node)
    queue = [node]
    safeGold = 0
    
    while queue:
        m = queue.pop(0)
        if grid[m[0]][m[1]] == "G":
            safeGold += 1
        trapNeighbour = False
        neighbours = []
        for i in range(m[0]-1, m[0]+2):
            for j in range(m[1]-1, m[1]+2):
                if abs(m[0]-i) ^ abs(m[1]-j):
                    neighbours.append((i, j))
        for neighbour in neighbours:
            if graph[neighbour[0]][neighbour[1]]== "T":
                trapNeighbour = True
        if not trapNeighbour:
            for neighbour in neighbours:
                if neighbour not in visited and graph[neighbour[0]][neighbour[1]] != "#":
                    visited.append(neighbour)
                    queue.append(neighbour)
    return safeGold

inp = input().split()
W, H = int(inp[0]), int(inp[1])

playerpos = 0
grid = [["" for i in range(W)] for j in range(H)]
for i in range(H):
    row = input()
    for j, tile in enumerate(row):
        if tile == 'P':
            playerpos = (i, j)
        grid[i][j] = tile
print(bfs([], grid, playerpos))
