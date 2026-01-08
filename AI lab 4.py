from collections import deque

def valid(s):
    ml, cl, _ = s
    mr = 3 - ml
    cr = 3 - cl
    if ml > 0 and cl > ml:
        return False
    if mr > 0 and cr > mr:
        return False
    return True

def next_states(s):
    ml, cl, b = s
    moves = [(2,0),(0,2),(1,1),(1,0),(0,1)]
    res = []

    for m, c in moves:
        if b == 0:
            ns = (ml - m, cl - c, 1)
        else:
            ns = (ml + m, cl + c, 0)

        if 0 <= ns[0] <= 3 and 0 <= ns[1] <= 3 and valid(ns):
            res.append(ns)

    return res

def solve():
    start = (3,3,0)
    goal = (0,0,1)
    q = deque([(start, [])])
    visited = set()

    while q:
        s, path = q.popleft()
        if s == goal:
            return path + [s]
        if s not in visited:
            visited.add(s)
            for n in next_states(s):
                q.append((n, path + [s]))

sol = solve()
for s in sol:
    print(s)

