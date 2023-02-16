# https://liu.kattis.com/problems/intervalcover
# Author: Oliver Green
"""
The program takes the following input:
Goal-interval to be covered, ex:                        -0.5 1
The amount of intervals to cover the goal, ex:          3
Next are three lines of the intervals to be used, ex:   -0.9 -0.1
                                                        -0.2 2
                                                        -0.7 1
The output is first the minimum amount of intervals that
needs to be used to cover the goal-interval.    ex:     1
Next output is the index of the intervals used. ex:     2
If the given intervals are impossible to combine to cover
the goal-interval, the output prints IMPOSSIBLE.

"""
import sys

"""
The function 'cover' takes the goal-interval and the given
intervals. Firstly a list of indices is created and sorted
according to the lowest value of an interval in the intervals
list.
The variable 'current' is a the current lower bound of the 
interval that still needs to be covered to cover the target interval.
The inner while loop then loops through all the given
intervals to find the one with the highest upper
bound that still covers the lowest point "current"
aswell. This maxinterval is then saved to the result 
and the current updates to match the new lower bound
of the interval left to cover to have the whole target
interval covered. This the repeats until current is
higher than the targets higher bound which
means that the whole target interval is covered
with the result. The function then returns
the indices of which intervals are used to
cover the target.

Complexity of the sorting at line 45 is O(n log(n))
Complexity of the nestled while loops are O(n log(n)) 
because the outer while loop is O(n) and has 
current < target as condition.
The inner while loop has the condition
intervals... <= current 
With these conditions the loops end up in O(n log(n))
"""
def cover(target, intervals): 
    indices = []
    result = []
    indices = sorted(range(len(intervals)), key=lambda x:intervals[x]) 
    current = target[0]     # 0
    index = 0
    while current < target[1] or not result:
        maxInterval = (current, -1)
        while index < len(intervals) and intervals[indices[index]][0] <= current: 
            maxInterval = max(maxInterval, (intervals[indices[index]][1], indices[index]))
            index += 1
        if maxInterval[1] == -1:
            return []
        current = maxInterval[0]
        result.append(maxInterval[1])
    return result


"""
This program reads the input and puts the goal-interval into 
the variable 'target' and the given intervals in the variable 'intervals'.
These are sent as parameters to the function 'cover'
Cover is only called once per testcase so it is only called a max of 30 times per run.
"""
target = (0, 0)
numOfIntervals = 0
intervals = []


for line in sys.stdin:
    if numOfIntervals == 0 and target == (0, 0):
        line = line.split()
        target = (float(line[0]), float(line[1]))
    elif target != (0, 0) and numOfIntervals == 0:
        numOfIntervals = int(line)
    else:
        line = line.split()
        intervals.append((float(line[0]), float(line[1])))
        numOfIntervals -= 1
        if numOfIntervals == 0:
            newSolution = cover(target, intervals)
            if not newSolution:
                print("impossible")
            else:
                print(len(newSolution))
                print(" ".join(str(i) for i in newSolution))
            target = (0, 0)
            intervals = []