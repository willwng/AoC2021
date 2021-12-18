import sys
from functools import lru_cache


def to_int(arr):
    return [int(a) for a in arr]



def solve(file_name):
    ans = 0
    with open(file_name) as f:
        for i, line in enumerate(f):
            l = line.strip()


    return ans


if __name__ == "__main__":
    file_name = str(sys.argv[1])
    ans = solve(file_name)
    print(f"Answer: {ans} ")
