import sys
import itertools 


def get_pixel(img, i, j, flip):
    if (i,j) not in img:
        return "0" if flip else "1"
    return "1" if flip else "0"

def get_bounds(img):
    return min([x for (x,y) in img]), max([x for (x,y) in img]), min([y for (x,y) in img]), max([y for (x,y) in img])

def enhance(img, algo, flip):
    dir = [-1, 0, 1]
    nearby = [p for p in itertools.product(dir, repeat=2)]

    min_x, max_x, min_y, max_y = get_bounds(img)
    margin = 10
    new_img = {}
    for i in range(min_x - margin, max_x + margin):
        for j in range(min_y - margin, max_y + margin):
            string = ""
            for dy, dx in nearby:
                string += get_pixel(img, i+dx, j+dy, flip)
            index = int(string, 2)
            rep = algo[index]
            
            if (rep == '#') != flip:
                new_img[(i,j)]='#'

    return new_img


def solve(file_name):
    ans1, ans2 = 0, 0
    algo, img = "", {}
    next = False
    y = 0
    with open(file_name) as f:
        for line in f:
            l = line.strip()
            if not l:
                next = True
                continue
            if not next:
                algo += l
            else:
                for x, c in enumerate(l):
                    if c == "#":
                        img[(x, y)] = c
                y += 1

    flip = True
    for n in range(50):
        if n == 2:
            ans1 = len(img.keys())
        img = enhance(img, algo, flip)
        flip ^= True #flipping flip!
    ans2 = len(img.keys())
   
    return ans1, ans2


if __name__ == "__main__":
    file_name = str(sys.argv[1])
    ans1, ans2 = solve(file_name)
    print(f"Answer 1: {ans1} ")
    print(f"Answer 2: {ans2} ")
