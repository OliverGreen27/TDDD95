
import math
import heapq

inp = input().split()
l, d, n = int(inp[0]), int(inp[1]), int(inp[2])

leftspike = 6
rightspike = l - 6

birdsplaced = 0

birdpositions = []
smallestpos = leftspike


for _ in range(n):
    heapq.heappush(birdpositions, int(input()))
print(birdpositions)
while smallestpos <= rightspike:
    if not birdpositions or abs(smallestpos - birdpositions[0]) / d >= 1:
        birdsplaced += 1
        print("placed bird at: ", smallestpos)
        smallestpos = smallestpos + d
        print(smallestpos)
    else:
        smallestpos = birdpositions[0] + d
        heapq.heappop(birdpositions)
        print(smallestpos)

print(birdsplaced)