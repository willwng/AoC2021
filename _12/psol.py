import sys
from sys import setrecursionlimit
setrecursionlimit(int(1e9))


def add(dic, key, val):
    if key not in dic:
        dic[key] = []
    dic[key].append(val)
    return


def dfs(s, adj, small, large, visited):
    if s == "end":
        return 1
    if s in small and s in visited:
        return 0  # not a path

    visited[s] = True
    dic_copy = visited.copy()
    p = 0
    for a in adj[s]:
        visited = dic_copy.copy()
        p += dfs(a, adj, small, large, visited)
        visited = dic_copy
    return p


def solve():
    ans = 0
    small = {}
    large = {}
    adj = {}
    file_name = str(sys.argv[1])
    with open(file_name) as f:
        for line in f:
            l = line.strip()
            caves = l.split("-")
            c1 = caves[0]
            c2 = caves[1]
            if c1.isupper():
                large[c1] = True
            else:
                small[c1] = True
            if c2.isupper():
                large[c2] = True
            else:
                small[c2] = True
            add(adj, c1, c2)
            add(adj, c2, c1)

    visited = {}
    paths = dfs("start", adj, small, large, visited)
    ans = paths

    return ans


if __name__ == "__main__":
    ans = solve()
    print(f"Answer 1: {ans} ")
