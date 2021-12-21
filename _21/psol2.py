import sys
import itertools 
from functools import lru_cache

# all possible moves and times they occur
dice = [1,2,3]
possible_rolls = list(itertools.product(dice,dice,dice))
occurences = {}
for (r1, r2, r3) in possible_rolls:
    move = r1 + r2 +r3
    if move in occurences:
        occurences[move] += 1
    else: 
        occurences[move] = 1


@lru_cache(maxsize=None)
def run(p1, p2, s1, s2):
    if s1 >= 21:
        return 1,0
    if s2 >= 21:
        return 0,1
    
    s1_old, p1_old = s1, p1
    ans1, ans2 = 0, 0
    for move in occurences:
        # reset
        p1, s1 = p1_old, s1_old
        # move
        p1 += move
        p1 = (p1 % 10)
        if p1 == 0:
            p1 = 10
            
        s1 += p1
        if s1 >= 21:
            ans1 += occurences[move]
        else:
            # switch sides
            win1, win2 = run(p2, p1, s2, s1)
            ans1 += win2 * occurences[move]
            ans2 += win1 * occurences[move]
    return ans1, ans2

def solve(p1, p2):
    ans = max(run(p1, p2, 0, 0))
    return ans

if __name__ == "__main__":
    ans = solve(6, 8)
    print(f"Answer 1: {ans} ")
