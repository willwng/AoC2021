import sys


def add(arr, dic, k, v):
    if k in dic:
        dic[k] = dic[k] | v
    else:
        arr.append((k, v))


def fold_x(paper, axis):
    to_add = []
    for (x, y) in paper:
        if x < axis:
            continue
        add(to_add, paper, (axis - (x-axis), y), paper[(x, y)])
        paper[(x, y)] = 0

    for (k, v) in to_add:
        paper[k] = v
    return


def fold_y(paper, axis):
    to_add = []
    for (x, y) in paper:
        if y < axis:
            continue
        add(to_add, paper, (x, axis - (y-axis)), paper[(x, y)])
        paper[(x, y)] = 0

    for (k, v) in to_add:
        paper[k] = v
    return


def solve():
    ans = 0
    paper = {}
    folds = []
    file_name = str(sys.argv[1])
    with open(file_name) as f:
        for line in f:
            l = line.strip()
            if l == '':
                continue
            elif "x" in l:
                folds.append(('x', int(l.split('=')[1])))
            elif "y" in l:
                folds.append(('y', int(l.split('=')[1])))
            else:
                pos = l.split(',')
                x, y = int(pos[0]), int(pos[1])
                paper[(x, y)] = 1

    for f, axis in folds:
        if f == 'x':
            fold_x(paper, axis)
        else:
            fold_y(paper, axis)
        break

    for p in paper:
        ans += paper[p]
    return ans


if __name__ == "__main__":
    ans = solve()
    print(f"Answer 1: {ans} ")
