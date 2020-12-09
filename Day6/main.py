with open("Day6/testData/input.txt") as f:
    input = f.read().strip().split('\n\n')

def yes_answers(input, fcn):
    for group in input:
        yield len(fcn(*(set(s) for s in group)))

input = [line.split() for line in input]

print("Solution 1: ", sum(yes_answers(input, set.union)))

print("Solution 2: ", sum(yes_answers(input, set.intersection)))