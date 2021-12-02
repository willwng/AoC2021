import sys

def solve():
  ans = 0
  prev = sys.maxsize
  with open('input.txt') as f:
    for line in f:
      curr = int(line)
      if(curr > prev):
        ans += 1
      prev = curr
  return ans

def solve2():
  ans = 0
  window = [sys.maxsize, sys.maxsize, sys.maxsize]
  with open('input.txt') as f:
    for line in f:
      curr = int(line)
      if(curr > window.pop(0)):
        ans += 1
      window.append(curr)
  return ans


if __name__ == "__main__":
  ans = solve()
  print(f"Answer: {ans} ")
  ans2 = solve2()
  print(f"Answer: {ans2} ")