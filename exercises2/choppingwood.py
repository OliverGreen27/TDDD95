
import sys
from heapq import heappush, heappop

num_of_lines = int(input())

v_degrees = [1] * (num_of_lines+1)
one_degreers = []
v_raw = [*map(int,sys.stdin)]

for v in v_raw:
    v_degrees[v-1] +=1

for i in range(num_of_lines):
    if v_degrees[i] == 1:
        heappush(one_degreers, i)

v_index = 0
error = False
result = []

while one_degreers and v_index < len(v_raw):
    v = v_raw[v_index] - 1
    min_leaf = heappop(one_degreers)
    result.append(min_leaf+1)
    v_degrees[min_leaf] = 0
    v_degrees[v] -= 1
    if v_degrees[v] == 1:
        heappush(one_degreers, v)

    v_index += 1
if sum(v_degrees) > 1:
    print("Error")
else:
    print('\n'.join(str(n) for n in result))