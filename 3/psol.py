import sys

def axc(arr):
  c0 = [0 for i in range(12)]
  c1 = [0 for i in range(12)]
  for line in arr:
    for i,v in enumerate(line):
      if v=='0':
        c0[i] += 1
      else:
        c1[i] += 1
  ans = [0 for i in range(12)]
  eps = [0 for i in range(12)]
  for i in range(len(c0)):
    if c0[i] > c1[i]:
      ans[i] = 0
      eps[i] = 1
    else:
      ans[i] = 1
      eps[i] = 0
  print(c0, c1, ans)
  return ans


def solve():
  c0 = [0 for i in range(12)]
  c1 = [0 for i in range(12)]
  with open('input.txt') as f:
    for line in f:

      line_r = list(line.strip())
      for i,v in enumerate(line_r):
        if v=='0':
          c0[i] += 1
        else:
          c1[i] += 1
  ans = [0 for i in range(12)]
  eps = [0 for i in range(12)]
  for i in range(len(c0)):
    if c0[i] > c1[i]:
      ans[i] = 0
      eps[i] = 1
    else:
      ans[i] = 1
      eps[i] = 0
  ans = [str(i) for i in ans]
  eps = [str(i) for i in eps]

  fin = ''.join(ans)
  eps = ''.join(eps)
  fin = int(fin, 2)
  eps = int(eps, 2)
  print(fin, eps)
  return fin*eps

def filter(arr, n, i):
  new = []
  for a in arr:
    if a[i] == str(n):
      new.append(a)
  return new

def solve2():
  all_nums = []
  c0 = [0 for i in range(12)]
  c1 = [0 for i in range(12)]
  with open('input.txt') as f:
    for line in f:
      line_r = list(line.strip())
      all_nums.append(line_r)

      for i,v in enumerate(line_r):
        if v=='0':
          c0[i] += 1
        else:
          c1[i] += 1
  ans = [0 for i in range(12)]
  eps = [0 for i in range(12)]
  for i in range(len(c0)):
    if c0[i] > c1[i]:
      ans[i] = 0
      eps[i] = 1
    else:
      ans[i] = 1
      eps[i] = 0

  cop = [i for i in all_nums]
  o = []
  c = []
  for i,a in enumerate(ans):
    ans = axc(all_nums)
    if(len(all_nums) == 1):
      o= int(''.join(all_nums[0]),2)
      break
    all_nums = filter(all_nums,  ans[i], i)
  o= int(''.join(all_nums[0]),2)

  ans = axc(cop)
  for i,a in enumerate(ans):
    if(len(cop) == 1):
      c= int(''.join(cop[0]),2)
      break
    cop = filter(cop, ans[i] ^ 1, i)
    ans = axc(cop)
  c= int(''.join(cop[0]),2)
  print(all_nums,cop)
  print(o, c)
  
  return o*c

if __name__ == "__main__":
  ans = solve()
  print(f"Answer 1: {ans} ")
  ans = solve2()
  print(f"Answer 2: {ans} ")
