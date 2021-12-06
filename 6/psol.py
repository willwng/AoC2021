import sys
from functools import lru_cache


dic = {}

def create(start, days):
    if start in dic:
        return dic[start]
    ans = 1
    i=start
    while i < days:
        ans += create(i + 9, days)
        i += 7
    if start not in dic:
        dic[start] = ans
    return ans

def solve():
    ans = 0
    days = 256
    fish = []
    with open('input.txt') as f:
        for line in f:
           fish = line.split(',')
           fish = list(map(int, fish))

    for i in fish:
        new_fish = create(i, days)
        ans += new_fish

    return ans

if __name__ == "__main__":
    ans = solve()
    print(f"Answer 1: {ans} ")

