import sys
from functools import lru_cache


@lru_cache
def sum_to(n):
    ans = n*(n+1)/2
    return ans


def solve():
    ans = 0

    with open('input.txt') as f:
        for line in f:
            arr = line.split(',')
        arr = [int(a) for a in arr]

    best = sys.maxsize
    for i in range(min(arr), max(arr) + 1):
        score = 0
        for a in arr:
            score += sum_to(abs(a - i))
        if score < best:
            best = score
            ans = score

    return ans


if __name__ == "__main__":
    ans = solve()
    print(f"Answer 1: {ans} ")
