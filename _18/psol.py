import sys
import numpy as np
from ast import literal_eval
import math
import itertools


def nested(l):
    left, right = 1, 1
    if isinstance(l[0], list):
        left =  1 + nested(l[0])
    if isinstance(l[1], list):
        right = 1 + nested(l[1])
    return max(left, right)
   
# add val to left or right side
def lr_reg(l, side, val):
    if isinstance(l, int):
        return l + val
    elif side == 0:
        return [lr_reg(l[0], side, val), l[1]]
    else:
        return [l[0], lr_reg(l[1], side, val)]

def explode(x, nest):
    if isinstance(x, int):
        return x, [0, 0], False
    elif nest == 0:
        l_add, r_add = x[0], x[1]
        return 0, [l_add, r_add], True
    
    left, right = x[0], x[1]
    left, add, l_change = explode(left, nest - 1)
    if l_change:
        return [left, lr_reg(right, 0, add[1])], [add[0], 0], True
    right, add, r_change = explode(right, nest - 1)
    if r_change:
        return [lr_reg(left, 1, add[0]), right], [0, add[1]], True
    return x, [0, 0], False

def split(s):
    if isinstance(s, int):
        if s >= 10:
            return [int(s/2), int(math.ceil(s/2))], True
        else:
            return s, False
    # list
    l, r = s[0], s[1]
    l, l_split = split(l)
    if l_split:
        return [l, r], True
    r, r_split = split(r)
    if r_split:
        return [l, r], True

    return s, False

def reduce(n):
    while True:
        n, _, change = explode(n, 4)
        if change:
            continue
        n, change = split(n)
        if not change:
            break
    return n

def magnitude(l):
    if isinstance(l, int):
        return l
    return 3*magnitude(l[0])+2*magnitude(l[1])

def solve1(nums):
    add = nums[0]
    for i in range(1, len(nums)):
        add = [add]
        add.append(nums[i])
        add = reduce(add)
    ans = magnitude(add)
    return ans

def solve2(nums):
    ans = 0
    for subset in itertools.permutations(nums, 2):
        add = [subset[0], subset[1]]
        add = reduce(add)
        if magnitude(add) > ans:
            ans = magnitude(add)
    return ans


if __name__ == "__main__":
    file_name = str(sys.argv[1])
    nums = []
    with open(file_name) as f:
        for line in f:
            l = line.strip()
            arr = np.array(literal_eval(l)).tolist()
            nums.append(arr)
    ans = solve1(nums)
    print(f"Answer 1: {ans} ")
    ans = solve2(nums)
    print(f"Answer 2: {ans} ")   