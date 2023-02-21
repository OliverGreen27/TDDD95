
import heapq
import math

inp = input().split()
l, d, n = int(inp[0]), int(inp[1]), int(inp[2])

leftspike = 6
rightspike = l - 6

totalbirdcount = n

birdpositions = []

nextsmallest = leftspike

def is_valid(pos):
    pass
def fill_gaps():
    for i, num in enumerate(birdpositions):
        if math.abs(num - birdpositions[i+1]) / d > 1 and math.abs(num - birdpositions[i+1]) % d:
            pass  

for _ in range(n):
    heapq.heappush(birdpositions, int(input()))
    if n > 1:
        fill_gaps()

print(birdpositions)