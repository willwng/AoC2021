import sys


def add(dic, key, val):
    if key not in dic:
        dic[key] = []
    dic[key].append(val)
    return


def dfs(s, adj, large, visited):
    if s == "end":
        return 1
    if not large[s] and s in visited:
        return 0  # not a path

    visited[s] = True
    dic_copy = visited.copy()
    p = 0
    for a in adj[s]:
        visited = dic_copy.copy()
        p += dfs(a, adj, large, visited)
        visited = dic_copy
    return p


def solve():
    ans = 0
    large, adj = {}, {}
    file_name = str(sys.argv[1])
    with open(file_name) as f:
        for line in f:
            l = line.strip()
            caves = l.split("-")
            large[caves[0]] = caves[0].isupper()
            large[caves[1]] = caves[1].isupper()
            add(adj, caves[0], caves[1])
            add(adj, caves[1], caves[0])

    visited = {}
    paths = dfs("start", adj, large, visited)
    ans = paths

    return ans


if __name__ == "__main__":
    ans = solve()
    print(f"Answer 1: {ans} ")
