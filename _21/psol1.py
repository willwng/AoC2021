import sys
import itertools 
from functools import lru_cache
import numpy as np
import heapq



def solve(p1, p2):
    ans = 0
    s1, s2 = 0, 0
    dice = 0
    rolls = 0
    while s1 < 1000 and s2 < 1000:
        for _ in range(3):
            dice += 1
            dice = (dice % 100)
            if dice == 0:
                dice = 100
            p1 += dice
            rolls += 1
        p1 = (p1 % 10)

        if p1 == 0:
            p1 = 10
        s1 += p1
        if s1 >= 1000:
            break       
        for _ in range(3):
            dice += 1
            dice = (dice % 100)
            if dice == 0:
                dice = 100
            p2 += dice
            rolls += 1
        p2 = (p2 % 10)
        if p2 == 0:
            p2 = 1
        s2 += p2   
        
    ans = min(s1, s2) * rolls
    return ans


if __name__ == "__main__":
    ans = solve(6, 8)
    print(f"Answer 1: {ans} ")
