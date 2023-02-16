# https://liu.kattis.com/problems/babelfish

import sys
d = dict()

inpuT = """dog ogday
cat atcay
pig igpay
froot ootfray
loops oopslay

atcay
ittenkay
oopslay
""".split('\n')

dictionaryPhase = True
for line in sys.stdin:
    line = line.strip()
    if not line:
        dictionaryPhase = False
    elif line and dictionaryPhase:
        splitted = line.split()
        d[splitted[1]] = splitted[0]
    else:
        if line in d:
            print(d[line])
        else: 
            print("eh")