import sys
import itertools 
from functools import lru_cache


def remove(x, dic):
    if x in dic:
        del[x]
    
def solve(file_name):
    ans = 0

    steps = []
    with open(file_name) as f:
        for line in f:
            l = line.strip()
            x = list(map(int,l.split("x=")[1].split(",")[0].split("..")))
            y = list(map(int,l.split("y=")[1].split(",")[0].split("..")))
            z = list(map(int,l.split("z=")[1].split("..")))
            on = True if "on" in l else False
            xl, xh = x[0], x[1]
            yl, yh = y[0], y[1]
            zl, zh = z[0], z[1]
            step = [on, (xl, xh), (yl, yh), (zl,zh)]
            steps.append(step)
    
    on_cubes = set()
    for i,step in enumerate(steps):
        on, (xl, xh), (yl, yh), (zl,zh) = step
        xl = max(-50, xl)
        yl = max(-50, yl)
        zl = max(-50, zl)
        xh = min(50, xh)
        yh = min(50, yh)
        zh = min(50, zh)
        print(f"step {i}")
        if on:  
            for x in range(xl, xh+1):
                for y in range(yl, yh+1):
                    for z in range(zl, zh+1):
                        on_cubes.add((x,y,z))
        else:
            remove = set()
            for (x,y,z) in on_cubes:
                if x >= xl and x <= xh and y >= yl and y <= yh and z >= zl and z <= zh:
                    remove.add((x,y,z))
            for (x,y,z) in remove:
                on_cubes.remove((x,y,z))
    ans = len(on_cubes)
    return ans


if __name__ == "__main__":
    file_name = str(sys.argv[1])
    ans = solve(file_name)
    print(f"Answer: {ans} ")
