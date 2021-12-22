import sys

def is_intersect(c1, c2):
    min_x1, max_x1, min_y1, max_y1, min_z1, max_z1, on = c1
    min_x2, max_x2, min_y2, max_y2, min_z2, max_z2, on = c2
    int_x = max_x2 >= min_x1 and min_x2 <= max_x1
    int_y = max_y2 >= min_y1 and min_y2 <= max_y1
    int_z = max_z2 >= min_z1 and min_z2 <= max_z1

    return int_x and int_y and int_z

# invariant: cuboids contains all non-intersecting cuboids
def interesect_cuboids(new, cuboids, add):
    min_x2, max_x2, min_y2, max_y2, min_z2,max_z2,on = new
    to_add = []
    for i in range(len(cuboids)):
        cuboid = cuboids[i]
        # slice and dice the old cuboid
        if(is_intersect(cuboids[i], new)):
            if cuboid[0] < min_x2:
                add = cuboid.copy()
                add[1] = min_x2
                to_add.append(add)
                cuboid[0] = min_x2
            if cuboid[1] > max_x2:
                add = cuboid.copy()
                add[0] = max_x2
                to_add.append(add)
                cuboid[1] = max_x2
            if cuboid[2] < min_y2:
                add = cuboid.copy()
                add[3] = min_y2
                to_add.append(add)
                cuboid[2] = min_y2
            if cuboid[3] > max_y2:
                add = cuboid.copy()
                add[2] = max_y2
                to_add.append(add)
                cuboid[3] = max_y2
            if cuboid[4] < min_z2:
                add = cuboid.copy()
                add[5] = min_z2
                to_add.append(add)
                cuboid[4] = min_z2
            if cuboid[5] > max_z2:
                add = cuboid.copy()
                add[4] = max_z2
                to_add.append(add)
                cuboid[5] = max_z2
        else:
            to_add.append(cuboid)
    if add:
        to_add.append(new)

    return to_add

def get_vol(cuboids):
    vol = 0
    for c in cuboids:
        x1, x2, y1, y2, z1, z2, on = c
        if on:
            vol += (x2-x1)*(y2-y1)*(z2-z1)
    return vol

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
            xl, xh = x[0], x[1]+1
            yl, yh = y[0], y[1]+1
            zl, zh = z[0], z[1]+1

            step = [on, (xl, xh), (yl, yh), (zl,zh)]
            steps.append(step)
    

    cuboids = []
    for i, step in enumerate(steps):
        on, (xl, xh), (yl, yh), (zl,zh) = step
        cuboid = [xl, xh, yl, yh, zl,zh, on]
        cuboids = interesect_cuboids(cuboid, cuboids, on)

    ans = get_vol(cuboids)
    return ans


if __name__ == "__main__":
    file_name = str(sys.argv[1])
    ans = solve(file_name)
    print(f"Answer: {ans} ")
