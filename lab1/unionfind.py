import time
start_time = time.time()

toprint = ""

def query(sets, a, b):
    global toprint
    if b in sets[a]:
        toprint += "yes\n"
    else:
        toprint += "no\n"

def joined(sets, a, b):
    merged = sets[a].union(sets[b])  # O(len(sets[a]) + len(sets[b])) absolut max 2 000 000
    for num in merged:
        sets[num] = merged
    return sets

inp = input().split()
N, Q = int(inp[0]), int(inp[1])

sets = [set([i]) for i in range(N)]
for _ in range(Q):
    line = input().split()
    if line[0] == "?":
        query(sets, int(line[1]), int(line[2]))
    elif line[0] == "=":
        sets = joined(sets, int(line[1]), int(line[2]))
    print("--- %s seconds ---" % (time.time() - start_time))
    
print(toprint)