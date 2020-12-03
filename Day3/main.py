from itertools import starmap
from math import prod

grid = [list(x.strip()) for x in open('Day3/testData/trees.txt').readlines()]

def trajectory(a, b):
    counter = 0
    i = j = 0

    while i < len(grid):
        if i < len(grid) and grid[i][j] == '#':
            counter += 1
        j = (j + b) % len(grid[i])
        i += a
    return counter


print('Solution1 :', prod(starmap(trajectory, [(1, 3)]))) #Part1
print('Solution2 :', prod(starmap(trajectory, [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]))) #Part2

