import sys
from queue import PriorityQueue


class Node:

    def __init__(self, i, j):
        self.i = i
        self.j = j
        self.dist = sys.maxsize
        self.neighbors = []

    def add_neighbor(self, n):
        self.neighbors.append(n)

    def __eq__(self, other):
        return (self.dist == other.dist)

    def __ne__(self, other):
        return (self.dist != other.dist)

    def __lt__(self, other):
        return (self.dist < other.dist)

    def __gt__(self, other):
        return (self.dist > other.dist)

    def __le__(self, other):
        return (self.dist <= other.dist)

    def __ge__(self, other):
        return (self.dist >= other.dist)


def solve(file_name):
    ans = sys.maxsize
    world = []
    with open(file_name) as f:
        for i, line in enumerate(f):
            l = list(line.strip())
            world.append([int(a) for a in l])

    new_world = []
    for i in range(len(world)):
        row = []
        for j in range(len(world[i])):
            row.append(Node(i, j))
        new_world.append(row)

    ex, ey = len(world)-1, len(world[0])-1
    frontier = PriorityQueue()
    new_world[0][0].dist = 0
    frontier.put(new_world[0][0])
    while not frontier.empty():
        g = frontier.get()
        dx = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for (x, y) in dx:
            vx = g.i + x
            vy = g.j + y
            if vx < 0 or vx >= len(world) or vy < 0 or vy >= len(world[0]):
                continue
            v = new_world[vx][vy]
            if g.dist + world[vx][vy] < v.dist:
                v.dist = g.dist + world[vx][vy]
                frontier.put(v)

        if g.i == ex and g.j == ey:
            ans = g.dist
            break

    return ans


if __name__ == "__main__":
    file_name = str(sys.argv[1])
    ans = solve(file_name)
    print(f"Answer 1: {ans} ")
