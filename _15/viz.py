import sys
from queue import PriorityQueue
import tkinter as tk
from functools import partial
import numpy as np


class Node:
    def __init__(self, i, j):
        self.i = i
        self.j = j
        self.dist = sys.maxsize
        self.color = -1  # -1 for white, 0 gray, 1 black
        self.path = []  # The shortest path of nodes taken to get to this node

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


def draw_world(c, world, new_world, v, event=None):
    c.delete("all")
    w = c.winfo_width()
    h = c.winfo_height()
    space_x = w / len(world)
    space_y = h / len(world[0])
    # Grid lines
    for i in range(len(world)):
        c.create_line([(i*space_x, 0), (i*space_x, h)])
    for j in range(len(world[0])):
        c.create_line([(0, j*space_y), (w, j*space_y)])

    # Colors
    for i in range(len(new_world)):
        for j in range(len(new_world[0])):
            if new_world[i][j].color == 0:
                c.create_rectangle(i*space_x, j*space_y, (i+1)
                                   * space_x, (j+1)*space_x, fill="gray")
            elif new_world[i][j].color == 1:
                c.create_rectangle(i*space_x, j*space_y, (i+1)
                                   * space_x, (j+1)*space_x, fill="black")
    # Color the path
    for node in v.path:
        i = node.i
        j = node.j
        c.create_rectangle(i*space_x, j*space_y, (i+1)
                           * space_x, (j+1)*space_x, fill="yellow")

    # Numbers
    for i in range(len(world)):
        for j in range(len(world[0])):
            c.create_text((i+0.5)*space_x, (j+0.5) *
                          space_y, text=str(world[i][j]))
    c.update()
    return


def create_big_row(row, n):
    new_row = [a for a in row]
    for _ in range(n):
        for i in range(len(new_row)):
            new_row[i] += 1
            if new_row[i] > 9:
                new_row[i] = 1
    return new_row


def create_big_world(tile):
    world = [[] for _ in range(5*len(tile))]
    for z in range(5):
        for r, row in enumerate(tile):
            for i in range(5):
                world[r+len(tile)*z].extend(create_big_row(row, i+z))
    return world


def solve(file_name):

    root = tk.Tk()
    c = tk.Canvas(root, height=800, width=800, bg='white')
    c.pack(fill=tk.BOTH, expand=True)

    ans = sys.maxsize
    # Loading and creating world
    world = []
    with open(file_name) as f:
        for i, line in enumerate(f):
            l = list(line.strip())
            world.append([int(a) for a in l])
    world = create_big_world(world)

    new_world = []
    for i in range(len(world)):
        row = []
        for j in range(len(world[i])):
            row.append(Node(i, j))
        new_world.append(row)

    # Dijkstra's
    ex, ey = len(world)-1, len(world[0])-1  # Final
    frontier = PriorityQueue()
    # Add root to PriorityQueue, set dist to 0, and color gray
    new_world[0][0].dist = 0
    new_world[0][0].color = 0
    new_world[0][0].path = []
    frontier.put(new_world[0][0])
    neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    while not frontier.empty():
        g = frontier.get()
        for (x, y) in neighbors:
            vx, vy = g.i + x, g.j + y
            # Out of bounds
            if vx < 0 or vx >= len(world) or vy < 0 or vy >= len(world[0]):
                continue
            # Get the neighboring node
            v = new_world[vx][vy]
            if g.dist + world[vx][vy] < v.dist:
                v.dist = g.dist + world[vx][vy]
                v.color = 0  # Gray
                v.path = g.path.copy()
                v.path.append(g)
                frontier.put(v)
            draw_world(c, world, new_world, v)

        # Color black
        g.color = 1

        if g.i == ex and g.j == ey:
            ans = g.dist
            break

    return ans


if __name__ == "__main__":
    file_name = str(sys.argv[1])
    ans = solve(file_name)
    print(f"Answer 1: {ans} ")
