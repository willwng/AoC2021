import sys
import binascii


def to_int(arr):
    return [int(a) for a in arr]


def get_set(string, i):
    ans = string[:i]
    string = string[i:]
    return ans, string


def parse_str(string):
    if string.replace("0", "") == "":
        return 0, ""
    vers, s = get_set(string, 3)
    id, s = get_set(s, 3)
    vers = int(vers, 2)
    id = int(id, 2)
    ans = vers
    if id == 4:
        curr, s = get_set(s, 5)
        lit = curr[1:]
        while curr[0] == "1":
            curr, s = get_set(s, 5)
            lit += curr[1:]
        lit = int(lit, 2)
        return vers, s
    else:
        length,s = get_set(s, 1)
        length = int(length, 2)
        if length == 0:
            sub_p,s = get_set(s, 15)
        else:
            sub_p,s = get_set(s, 11)
        sub_p = int(sub_p, 2)
        for _ in range(sub_p):
            v, s = parse_str(s)
            ans += v
        return ans, s
            

def solve(file_name):
    ans = 0
    with open(file_name) as f:
        for i, line in enumerate(f):
            l = line.strip()
            b_str = bin(int(l, 16))[2:].zfill(len(l) * 4)


    vers_sum, s = parse_str(b_str)
    ans = vers_sum
    return ans


if __name__ == "__main__":
    file_name = str(sys.argv[1])
    ans = solve(file_name)
    print(f"Answer: {ans} ")
