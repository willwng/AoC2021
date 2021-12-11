def flash(flashed, octopodes, i, j):
    if (i, j) in flashed:
        return
    if i < 0 or i >= len(octopodes):
        return
    if j < 0 or j >= len(octopodes):
        return
    octopodes[i][j] += 1
    if octopodes[i][j] <= 9:
        return

    flashed[(i, j)] = True

    flash(flashed, octopodes, i+1, j)
    flash(flashed, octopodes, i+1, j-1)
    flash(flashed, octopodes, i+1, j+1)
    flash(flashed, octopodes, i, j-1)
    flash(flashed, octopodes, i, j+1)
    flash(flashed, octopodes, i-1, j)
    flash(flashed, octopodes, i-1, j-1)
    flash(flashed, octopodes, i-1, j+1)
    return


def solve():
    octopodes = []
    with open('input.txt') as f:
        for line in f:
            l = line.strip()
            l_arr = list(l)
            l_arr = [int(a) for a in l_arr]
            octopodes.append(l_arr)

    step = 1
    while True:
        flashed = {}
        for i in range(len(octopodes)):
            for j in range(len(octopodes[i])):
                flash(flashed, octopodes, i, j)
        if len(flashed) == len(octopodes) * len(octopodes[0]):
            return step
        for (i, j) in flashed:
            octopodes[i][j] = 0
        step += 1


if __name__ == "__main__":
    ans = solve()
    print(f"Answer 2: {ans} ")
