import sys
from functools import lru_cache
from statistics import median

points = {}
points[')'] = 1
points[']'] = 2
points['}'] = 3
points['>'] = 4

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
                return -1
    while stack:
        ans *= 5
        ans += points[corr[stack.pop()]]
    return ans


def solve():
    ans = 0
    answers = []
    with open('input.txt') as f:
        for line in f:
            if solve_line(line.strip()) != -1:
                answers.append(solve_line(line.strip()))

    ans = median(answers)
    return ans


if __name__ == "__main__":
    ans = solve()
    print(f"Answer 1: {ans} ")
