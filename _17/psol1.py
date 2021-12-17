import sys
from functools import lru_cache
import numpy as np


def to_int(arr):
    return [int(a) for a in arr]


def in_bounds(bounds, x, y):
    return x >= bounds[0] and x <= bounds[1] and y >= bounds[2] and y <= bounds[3]


def run(bounds, vx, vy):
    px, py = 0, 0
    max_y = 0
    for s in range(500):
        px += vx
        py += vy
        vy = vy - 1
        if py > max_y:
            max_y = py
        if vx > 0:
            vx -=1
        elif vx < 0:
            vx += 1

        
        if(in_bounds(bounds, px, py)):
            return True, max_y
        if py < bounds[2]:
            return False, 0
    return False, 0

def solve(file_name):
    ans = 0
    with open(file_name) as f:
        for i, line in enumerate(f):
            l = line.strip()
            [x_min, x_max, y_max, y_min] = l.split(',')
            bounds = [x_min, x_max, y_max, y_min]
            bounds = to_int(bounds)

    pos_x, pos_y = 0, 0
    max_y = 0
    for v_x in range(500):
        for v_y in range(-150,500):
            r, my = run(bounds, v_x, v_y)
            if r and my > max_y:
                max_y = my
    r, my = run(bounds, 7, 2)

    ans = max_y
    return ans


if __name__ == "__main__":
    file_name = str(sys.argv[1])
    ans = solve(file_name)
    print(f"Answer: {ans} ")
