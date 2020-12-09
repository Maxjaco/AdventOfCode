p, C, N = 25, [], [int(n) for n in open('Day9/testData/input.txt')]

is_ok = lambda n, S: any(True for j in range(p) if n-S[j] in S[j+1:])

x = next(n for i,n in enumerate(N[p:]) if not is_ok(n, sorted(N[i:i+p])))

for n in N:
    C += [n]
    while sum(C) > x: C.pop(0)
    if len(C) > 1 and sum(C) == x: break
        
print('Part 1:', x, '\nPart 2:', min(C)+max(C))