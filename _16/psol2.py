import sys
import binascii


def to_int(arr):
    return [int(a) for a in arr]


def get_set(string, i):
    ans = string[:i]
    string = string[i:]
    return ans, string


def parse_str(string):
    # Version and id 
    vers, s = get_set(string, 3)
    id, s = get_set(s, 3)
    vers, id = int(vers, 2), int(id, 2)

    if id == 4:
        lit = ""
        while True:
            curr, s = get_set(s, 5) 
            lit += curr[1:]
            if curr[0] == "0":
                break
        lit = int(lit, 2)
        return lit, s
    else:
        # Get length 0 or 1
        l, s = get_set(s, 1)       
        l = int(l, 2)    
        vs = []
        # Length or num subpackets
        if l == 0:
            length, s = get_set(s, 15)
            length = int(length, 2)
            sub_packets, s = get_set(s, length)
            while sub_packets != "":
                v, sub_packets = parse_str(sub_packets)
                vs.append(v)
        else:
            n_packets, s = get_set(s, 11)
            n_packets = int(n_packets, 2)
            for _ in range(n_packets):
                v, s = parse_str(s)
                vs.append(v)
        # go
        if id == 0:
            ans = sum(vs)
        elif id == 1:
            ans = 1
            for v in vs:
                ans *= v
        elif id == 2:
            ans = min(vs)
        elif id == 3:
            ans = max(vs)
        elif id == 5:
            ans = 1 if vs[0] > vs[1] else 0
        elif id == 6:
            ans = 1 if vs[0] < vs[1] else 0
        elif id == 7:
            ans = 1 if vs[0] == vs[1] else 0
        return ans, s
            

def solve(file_name):
    ans = 0
    with open(file_name) as f:
        for line in f:
            l = line.strip()
            b_str = bin(int(l, 16))[2:].zfill(len(l) * 4)
    ans, _, = parse_str(b_str)
    return ans


if __name__ == "__main__":
    file_name = str(sys.argv[1])
    ans = solve(file_name)
    print(f"Answer: {ans} ")
