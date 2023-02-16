
import sys
import heapq

myinp = """7
1
7
1""".split('\n')


inp = input().split()

candy, childAmount = int(inp[0]), int(inp[1])

heap = []
children = {0:0}
"""
for line in myinp:
    childWant = int(line)
    if childWant not in children:
        heapq.heappush(heap, -childWant)
    children[childWant] = children.get(childWant, 0)+1
    
"""

for i in range(childAmount):
    childWant = int(input())
    children[childWant] = children.get(childWant, 0) + 1
    
for childWant in children:
    heapq.heappush(heap, -childWant)

while candy > 0:
    maxWant = -heapq.heappop(heap)
    n = children.pop(maxWant)
    nextMaxWant = -heap[0]

    diff = maxWant - nextMaxWant
    if candy >= n*diff:
        try:
            children[nextMaxWant] += n
        except:
            print("error",children)
        candy -= n*diff
    
    elif candy >= n:
        newDiff = candy//n
        children[maxWant-newDiff] = n
        heapq.heappush(heap, -(maxWant-newDiff))
        candy -= n*newDiff
    else:
        children[maxWant-1] = children.get(maxWant-1, 0) + candy
        children[maxWant] = n - candy
        candy = 0

anger = 0
for wantAmount in children:
    anger += wantAmount**2 * children[wantAmount]

print(anger)