import sys

def solve():
  horizontal, depth = 0, 0
  with open('input.txt') as f:
    for line in f:
      line_arr = line.split(" ")
      command = line_arr[0]
      
      amount = int(line_arr[1])
      if command == "forward":
        horizontal += amount
      elif command == "down":
        depth += amount
      elif command == "up":
        depth -= amount
  return horizontal*depth

def solve2():
  horizontal, depth, aim = 0, 0, 0
  with open('input.txt') as f:
    for line in f:
      line_arr = line.split(" ")
      command = line_arr[0]
      amount = int(line_arr[1])
      if command == "forward":
        horizontal += amount
        depth += aim * amount
      elif command == "down":
        aim += amount
      elif command == "up":
        aim -= amount
  return horizontal*depth  

if __name__ == "__main__":
  ans = solve()
  print(f"Answer 1: {ans} ")
  ans = solve2()
  print(f"Answer 2: {ans} ")
