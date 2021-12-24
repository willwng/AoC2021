import sys
from functools import lru_cache

def verify(num, abcs):
    x, y, z = 0, 0, 0
    for i, (a,b,c) in enumerate(abcs):
        n = num // (10**(13-i))
        if n == 0:
            return False
        x = z
        x %= 26
        z //= a
        x += b
        x = int(x == n)
        x = int(x == 0)
        y = 25
        y *= x
        y += 1
        z *= y
        y = n
        y += c
        y *= x
        z += y
        num %= (10**(13-i))
    return z==0

def find_largest(constraints):
    num = [0 for _ in range(14)]
    for n_large, n_small, diff in constraints:
        num[n_small] = 9 - diff
        num[n_large] = 9
    return int("".join(map(str, num)))

def find_smallest(constraints):
    num = [0 for _ in range(14)]
    for n_large, n_small, diff in constraints:
        num[n_small] = 1
        num[n_large] = 1 + diff
    return int("".join(map(str, num)))

def solve(file_name):
    # Reading in input
    abcs = []
    count = -1
    prev = ""
    with open(file_name) as f:
        for i, line in enumerate(f):
            l = line.strip()
            if "inp" in l:
                if count > -1:
                    abcs.append(list(map(int,abc)))
                abc = []
                count += 1
            elif "div z" in l:
                abc.append(int(l.split("div z ")[1]))
            elif "add x" in l and "z" not in l:
                abc.append(int(l.split("add x ")[1]))
            elif "add y" and "add y w" in prev: # next line is important
                abc.append(int(l.split("add y ")[1]))   
            prev = l
    # Get the numbers that actually change
    abcs.append(list(map(int,abc)))
    check_offsets = [(b,c) for (_,b,c) in abcs]
    # Get the constraints
    stack = []
    constraints = []
    for i, (check, offset) in enumerate(check_offsets):
        if check > 0:
            stack.append((i, offset))
        else:
            popped = stack.pop()
            if popped[1] + check > 0:
                constraints.append((i, popped[0], popped[1] + check))
            else:
                constraints.append((popped[0], i, -1*(popped[1] + check)))
    # solve
    ans1 = find_largest(constraints)
    ans2 = find_smallest(constraints)
    assert(verify(ans1, abcs))
    assert(verify(ans2, abcs))

    return ans1, ans2


if __name__ == "__main__":
    file_name = str(sys.argv[1])
    ans1, ans2 = solve(file_name)
    print(f"Answer 1: {ans1} ")
    print(f"Answer 2: {ans2} ")
