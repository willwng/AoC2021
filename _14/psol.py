import sys


def add(dic, k, v):
    if k in dic:
        dic[k] += v
    else:
        dic[k] = v
    if dic[k] == 0:
        del dic[k]


def apply_insert(to_add, rule, ins, pairs, counts):
    if rule in pairs:
        count = pairs[rule]
        p_1 = rule[0] + ins
        p_2 = ins + rule[1]
        add(to_add, p_1, count)
        add(to_add, p_2, count)
        add(to_add, rule, -1 * count)
        add(counts, ins, count)
    return


def solve(file_name):
    ans = 0
    rules = {}
    with open(file_name) as f:
        for i, line in enumerate(f):
            l = line.strip()
            if i == 0:
                start_string = l
            elif i > 1:
                p = l.split(" -> ")
                rules[p[0]] = p[1]

    # num pairs, chars
    pairs, counts = {}, {}
    for i in range(len(start_string) - 1):
        add(pairs, start_string[i:i+2], 1)
        add(counts, start_string[i], 1)
    add(counts, start_string[-1], 1)

    # run steps
    steps = 40
    for _ in range(steps):
        to_add = {}
        for rule in rules:
            apply_insert(to_add, rule, rules[rule], pairs, counts)
        for a in to_add:
            add(pairs, a, to_add[a])

    # get ans
    maxv, minv = 0, sys.maxsize
    for c in counts:
        if counts[c] > maxv:
            maxv = counts[c]
        if counts[c] < minv:
            minv = counts[c]
    ans = maxv - minv
    return ans


if __name__ == "__main__":
    file_name = str(sys.argv[1])
    ans = solve(file_name)
    print(f"Answer 1: {ans} ")
