import sys
from functools import lru_cache


points = {}
points[')'] = 3
points[']'] = 57
points['}'] = 1197
points['>'] = 25137

corr = {}
corr['('] = ')'
corr['['] = ']'
corr['{'] = '}'
corr['<'] = '>'


def solve_line(line):
    stack = []
    ans = 0
    for c in line:
        if c in corr:
            stack.append(c)
        else:
            correct = corr[stack.pop()]
            if c != correct:
                ans += points[c]
                return ans
    return ans


def solve():
    ans = 0
    with open('input.txt') as f:
        for line in f:
            ans += solve_line(line.strip())

    return ans


if __name__ == "__main__":
    ans = solve()
    print(f"Answer 1: {ans} ")
