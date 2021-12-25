import sys
from functools import lru_cache
import numpy as np

def fix(a):
    if a == ".":
        return 0
    elif a == ">":
        return 1
    else:
        return -1

def step(world):
    moved = {}
    for i in range(len(world)):
        for j in range(len(world[i])):
            if world[i][j] == 0:
                continue
            if world[i][j] == 1:
                newx = j+1
                newy = i
                if newx >= len(world[i]):
                    newx = 0
                if world[newy][newx] == 0:
                    moved[(i,j)] = (1, newx, newy)

    
    for (i,j) in moved:
        world[i][j] = 0
        v, newx, newy = moved[(i,j)]
        world[newy][newx] = v

    for i in range(len(world)):
        for j in range(len(world[i])):
            if world[i][j] == 0:
                continue
            if world[i][j] == -1:
                newx = j
                newy = i+1
                if newy >= len(world):
                    newy = 0
                if world[newy][newx] == 0:
                    moved[(i,j)] = (-1, newx, newy)
    
    for (i,j) in moved:
        world[i][j] = 0
        v, newx, newy = moved[(i,j)]
        world[newy][newx] = v
    return moved


def solve(file_name):
    ans = 0
    world = []
    with open(file_name) as f:
        for y, line in enumerate(f):
            l = line.strip()
            row = list(l)
            world.append(list(map(fix, row)))
    steps=  1
    while(len(step(world)) != 0):
        steps += 1
    ans = steps

    return ans


if __name__ == "__main__":
    file_name = str(sys.argv[1])
    ans = solve(file_name)
    print(f"Answer: {ans} ")
