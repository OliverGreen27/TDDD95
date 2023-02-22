
import sys
import itertools

def perm(seq, n):
    perms = []
    print(seq)
    for p in itertools.product(seq, repeat=n):
        subcart = ("".join(p))
        perms.append(subcart)
    return perms


lperm = 0
for line in sys.stdin:
    inp = line.split()
    k, n = int(inp[0]), int(inp[1])
    strcomb = "".join(str(i) for i in range(k+1))
    lperm = perm(strcomb, n)
totalwords = len(lperm)
tightwords = 0
"""
for word in list(lperm):
    tight = True
    for i, c in enumerate(word):
        if i < len(word) - 1 and abs(int(c) - int(word[i+1])) > 1:
            tight = False
    if tight:
        tightwords += 1
"""
print(totalwords)
print(tightwords)
print(round(100* tightwords/totalwords, 9))