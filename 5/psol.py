import sys


def solve():
    board = [[0 for x in range(1000)] for y in range(1000)]
    with open('input.txt') as f:
        for line in f:
            c = line.strip().split('->')
            c1 = c[0].strip().split(',')
            c2 = c[1].strip().split(',')
            c1 = [int(i) for i in c1]
            c2 = [int(i) for i in c2]
            if(c1[0] == c2[0]):
                for i in range(min(c1[1], c2[1]), max(c1[1], c2[1])+1):
                    board[c1[0]][i] += 1
            elif(c1[1] == c2[1]):
                for i in range(min(c1[0], c2[0]), max(c1[0], c2[0])+1):
                    board[i][c1[1]] += 1
            else:
                i = 0
                startx = c1[0]
                starty = c1[1]
                dx = -1 if c1[0] > c2[0] else 1
                dy = -1 if c1[1] > c2[1] else 1
                iter = max(c1[0], c2[0]) - min(c1[0], c2[0]) + 1
                for i in range(iter):
                    board[startx][starty] += 1
                    startx += dx
                    starty += dy

    ans = 0
    for lst in board:
        for x in lst:
            if x >= 2:
                ans += 1

    return ans


def solve2():
    return 0


if __name__ == "__main__":
    ans = solve()
    print(f"Answer 1: {ans} ")
    ans = solve2()
    print(f"Answer 2: {ans} ")
